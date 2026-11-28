"""
Generator data SIMULASI untuk kajian churn pelanggan internet rumah
di tengah perang harga 2026.

Tidak ada data pelanggan sungguhan di sini. Parameter dikalibrasi dengan kondisi
pasar internet rumah (fixed broadband) Indonesia 2025-2026 supaya pola dan
skalanya realistis.

Satu baris = satu pelanggan residensial aktif per 1 Januari 2026.
Label `churn` = 1 jika pelanggan berhenti berlangganan (putus/pindah ISP) dalam
6 bulan pengamatan (Januari-Juni 2026, simulasi).

KALIBRASI (sumber Indonesia, lihat halaman showcase untuk tautan)
- Tagihan rata-rata ~Rp200-250 ribu: ARPU fixed broadband IndiHome Rp204-238 ribu.
- Harga paket 2026: 100 Mbps umumnya Rp229-375 ribu; sejak Feb 2026 muncul
  paket 100 Mbps Rp100 ribu (Internet Rakyat, MyRepublic Air) di sebagian wilayah.
- Kecepatan nyata: median fixed broadband Indonesia ~40 Mbps (Ookla, Agustus 2025);
  target Komdigi 45 Mbps (2026) -> kecepatan aktual sering di bawah paket.
- Bundling seluler (FMC) ~55-59% pelanggan IndiHome.
- Standar penanganan gangguan 1x24 jam.
- Loyalitas: 87,48% pelanggan tidak pernah ganti ISP (APJII 2025) -> churn
  6 bulan disimulasikan ~15% (lebih tinggi dari biasanya karena perang harga 2026).
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(2026)
N = 3000

KOTA = {  # porsi pelanggan, peluang ada kompetitor Rp100rb di area (2026)
    'Jakarta': (.24, .55), 'Kota Bekasi': (.12, .60), 'Kota Tangerang': (.11, .55), 'Kota Depok': (.09, .50),
    'Kota Bogor': (.08, .40), 'Kota Bandung': (.18, .45), 'Surabaya': (.18, .50),
}
PAKET = {  # Mbps: (porsi, harga/bulan termasuk PPN)
    20: (.10, 175_000), 30: (.30, 205_000), 50: (.32, 245_000), 100: (.22, 315_000), 200: (.06, 455_000),
}
BAYAR = {'Auto-debit / kartu kredit': .18, 'Virtual account bank': .38, 'E-wallet': .24, 'Gerai minimarket': .20}


def pick(opts, probs, n=None):
    p = np.array(probs, dtype=float); p /= p.sum()
    return RNG.choice(opts, size=n, p=p) if n else RNG.choice(opts, p=p)


def generate(n=N):
    rows = []
    for i in range(n):
        kota = pick(list(KOTA), [v[0] for v in KOTA.values()])
        mbps = int(pick(list(PAKET), [v[0] for v in PAKET.values()]))
        harga = PAKET[mbps][1]
        tv = int(RNG.random() < (.18 if mbps >= 50 else .08))
        fmc = int(RNG.random() < .50)                                  # bundling paket seluler
        tenure = int(np.clip(RNG.gamma(1.4, 18), 1, 120))              # bulan berlangganan
        kontrak = pick(['Bulanan (tanpa kontrak)', 'Kontrak 12 bulan', 'Kontrak 24 bulan'], [.45, .40, .15])
        sisa = None
        if kontrak != 'Bulanan (tanpa kontrak)':
            dur = 12 if '12' in kontrak else 24
            sisa = int((dur - tenure % dur) % dur)
        promo_habis = int(tenure <= 15 and RNG.random() < .35)         # harga promo baru berakhir (3 bln terakhir)
        diskon = 0.15 if promo_habis == 0 and tenure <= 6 and RNG.random() < .5 else 0.0
        tagihan = int(round(harga * (1 - diskon) + tv * 75_000 - fmc * 15_000, -3))
        bayar = pick(list(BAYAR), list(BAYAR.values()))
        kompetitor = int(RNG.random() < KOTA[kota][1])

        # kualitas layanan (3 bulan terakhir)
        kualitas_area = RNG.normal(0, 1)                                # infrastruktur lokal (tak teramati langsung)
        gangguan = int(RNG.poisson(np.exp(0.2 + 0.45 * kualitas_area)))
        jam_perbaikan = float(np.clip(RNG.lognormal(np.log(16), .6) * (1.25 if gangguan > 2 else 1), 2, 120)) if gangguan else 0.0
        kecepatan_pct = float(np.clip(RNG.normal(82, 14) - 6 * kualitas_area - (8 if mbps >= 100 else 0), 25, 105))
        keluhan_cs = int(RNG.poisson(0.35 + 0.55 * gangguan))
        telat = int(RNG.poisson({'Auto-debit / kartu kredit': .05, 'Virtual account bank': .45, 'E-wallet': .35, 'Gerai minimarket': .75}[bayar]))
        isolir = int(RNG.binomial(telat, .25)) if telat else 0
        pemakaian = float(np.clip(RNG.lognormal(np.log(180 + 2.2 * mbps), .55), 15, 2000))   # GB/bulan
        csat_true = 7.6 - 0.55 * gangguan - 0.02 * max(jam_perbaikan - 24, 0) + 0.04 * (kecepatan_pct - 80) + RNG.normal(0, 1.1)
        csat = int(np.clip(round(csat_true), 0, 10))

        # ---- logit churn 6 bulan ----
        z = (-3.25
             + 0.32 * gangguan + 0.018 * max(jam_perbaikan - 24, 0)
             - 0.025 * (kecepatan_pct - 80)
             + 0.25 * keluhan_cs
             + 1.1 * np.log(tagihan / 1000 / mbps / 5)                     # harga per Mbps relatif (value for money)
             + 0.85 * promo_habis
             + {'Bulanan (tanpa kontrak)': 0.35, 'Kontrak 12 bulan': 0.0, 'Kontrak 24 bulan': -0.25}[kontrak]
             + (0.9 if sisa is not None and sisa <= 1 else (-0.4 if sisa is not None and sisa >= 4 else 0.0))
             + (0.55 if tenure <= 6 else 0.25 if tenure <= 12 else -0.25 if tenure >= 48 else 0.0)
             - 0.55 * fmc - 0.35 * tv
             + {'Auto-debit / kartu kredit': -0.45, 'Virtual account bank': 0.0, 'E-wallet': 0.1, 'Gerai minimarket': 0.3}[bayar]
             + 0.22 * telat + 0.35 * isolir
             + 0.75 * kompetitor
             - 0.35 * np.log(pemakaian / 250)
             - 0.12 * (csat - 7)
             + RNG.normal(0, 0.35))
        p = 1 / (1 + np.exp(-z))
        rows.append(dict(
            kota=kota, paket_mbps=mbps, tagihan_bulanan=tagihan, add_on_tv=tv, bundling_seluler=fmc,
            lama_langganan_bulan=tenure, jenis_kontrak=kontrak, sisa_kontrak_bulan=sisa, promo_baru_berakhir=promo_habis,
            metode_bayar=bayar, kompetitor_murah_di_area=kompetitor,
            gangguan_3bln=gangguan, rata_jam_perbaikan=round(jam_perbaikan, 1), kecepatan_aktual_pct=round(kecepatan_pct, 1),
            keluhan_cs_3bln=keluhan_cs, telat_bayar_6bln=telat, isolir_6bln=isolir, pemakaian_gb_bulan=round(pemakaian),
            skor_kepuasan=csat, churn=int(RNG.random() < p),
        ))
    df = pd.DataFrame(rows)
    df.loc[RNG.random(len(df)) < 0.12, 'skor_kepuasan'] = np.nan          # tidak semua pelanggan mengisi survei
    df.insert(0, 'id_pelanggan', [f'PL{200001 + i}' for i in range(len(df))])
    return df


if __name__ == '__main__':
    df = generate()
    df.to_csv('data/pelanggan_internet_rumah_2026.csv', index=False)
    print(df.shape, f"churn 6 bulan {df.churn.mean():.1%} | tagihan rata-rata Rp{df.tagihan_bulanan.mean():,.0f}")
