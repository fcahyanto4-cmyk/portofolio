"""
Generator data SIMULASI untuk kajian risiko resign karyawan ritel modern
(Jabodetabek, Bandung, Surabaya).

Tidak ada data karyawan sungguhan di sini. Setiap parameter dikalibrasi dengan
statistik & regulasi Indonesia (lihat KALIBRASI di bawah) supaya pola dan
skalanya menyerupai kondisi ritel modern di kota besar Indonesia.

Satu baris = satu karyawan aktif per 1 Januari 2026.
Label `resign` = 1 jika karyawan mengundurkan diri secara sukarela dalam 12 bulan
pengamatan (simulasi). PHK, pensiun, dan habis kontrak tanpa perpanjangan dari
perusahaan TIDAK dihitung sebagai resign.

KALIBRASI (sumber Indonesia)
- UMK/UMP 2026 per kota (SK Gubernur, dirangkum Kemnaker/media nasional):
  gaji karyawan formal tidak boleh di bawah UMK.
- PP 35/2021: lembur maks 4 jam/hari & 18 jam/minggu -> dibatasi 72 jam/bulan;
  PKWT (kontrak) maks 5 tahun.
- Survei Komuter Jabodetabek BPS 2023: rata-rata waktu tempuh ~31 menit.
- Turnover ritel Indonesia: studi lokal melaporkan 11-35% per tahun (lihat
  halaman showcase). Target simulasi: ~19% resign sukarela per tahun,
  frontliner toko lebih tinggi, kantor pusat lebih rendah.
- Arah pengaruh faktor: studi turnover ritel Indonesia (jam kerja/lembur +,
  kompensasi -, stres/burnout +, jalur karier & hubungan atasan).
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(2026)
N = 2400

# UMK/UMP 2026 (Rp/bulan)
UMK = {
    'Jakarta': 5_729_876,
    'Kota Bekasi': 5_999_443,
    'Kota Tangerang': 5_399_405,
    'Kota Depok': 5_522_662,
    'Kota Bogor': 5_437_203,
    'Kota Bandung': 4_737_678,
    'Surabaya': 5_288_796,
}
JABODETABEK = {'Jakarta', 'Kota Bekasi', 'Kota Tangerang', 'Kota Depok', 'Kota Bogor'}

# jabatan: unit, level, porsi, rentang gaji (x UMK), offset risiko, status [PKWTT, PKWT, Outsourcing],
#          rata-rata lembur (jam/bulan), peluang shift malam, rata-rata masa kerja (th)
JABATAN = {
    'Kasir':                 ('Toko', 'Staf', .24, (1.00, 1.10), .45, (.25, .55, .20), 22, .35, 2.2),
    'Pramuniaga':            ('Toko', 'Staf', .26, (1.00, 1.08), .45, (.20, .50, .30), 20, .35, 2.0),
    'Kepala Toko':           ('Toko', 'Supervisor', .08, (1.35, 1.80), .35, (.85, .15, 0), 30, .15, 6.0),
    'Staf Gudang':           ('Gudang/DC', 'Staf', .12, (1.00, 1.12), .30, (.25, .40, .35), 28, .50, 2.8),
    'Driver Pengiriman':     ('Gudang/DC', 'Staf', .07, (1.02, 1.15), .35, (.30, .40, .30), 30, .20, 3.0),
    'Supervisor Gudang':     ('Gudang/DC', 'Supervisor', .03, (1.40, 1.90), .60, (.85, .15, 0), 25, .30, 6.5),
    'Area Manager':          ('Toko', 'Manajer', .02, (2.60, 3.80), 1.00, (1, 0, 0), 18, 0, 8.0),
    'Staf Admin & Keuangan': ('Kantor Pusat', 'Staf', .07, (1.15, 1.60), .80, (.60, .40, 0), 10, 0, 4.0),
    'Staf IT & Data':        ('Kantor Pusat', 'Staf', .04, (1.50, 2.40), 1.85, (.60, .40, 0), 14, 0, 3.0),
    'Staf Marketing':        ('Kantor Pusat', 'Staf', .04, (1.30, 2.00), .90, (.60, .40, 0), 12, 0, 3.0),
    'Manajer Kantor Pusat':  ('Kantor Pusat', 'Manajer', .03, (3.00, 5.00), 1.00, (1, 0, 0), 15, 0, 8.0),
}


def pick(options, probs, n):
    return RNG.choice(options, size=n, p=np.array(probs) / np.sum(probs))


def generate(n=N):
    names = list(JABATAN)
    jabatan = pick(names, [JABATAN[j][2] for j in names], n)
    rows = []
    for j in jabatan:
        unit, level, _, (gmin, gmax), off, st, lem, night, tenure = JABATAN[j]
        # lokasi
        if unit == 'Kantor Pusat':
            lokasi = 'Jakarta'
        elif unit == 'Gudang/DC':
            lokasi = pick(['Kota Bekasi', 'Kota Tangerang', 'Kota Bandung', 'Surabaya'], [.35, .30, .15, .20], 1)[0]
        else:
            lokasi = pick(list(UMK), [.30, .12, .12, .10, .08, .14, .14], 1)[0]
        status = pick(['PKWTT (tetap)', 'PKWT (kontrak)', 'Outsourcing'], st, 1)[0]

        # masa kerja (tahun) -- frontliner pendek, PKWT maks 5 tahun (PP 35/2021)
        masa = float(RNG.gamma(1.3, tenure / 1.3))
        if status == 'PKWT (kontrak)':
            masa = min(masa, RNG.uniform(0.1, 5.0))
        masa = round(min(max(masa, 0.1), 30), 1)
        sisa_kontrak = int(RNG.integers(0, 13)) if status == 'PKWT (kontrak)' else None

        # gaji: >= UMK, naik sedikit sesuai masa kerja
        mult = RNG.uniform(gmin, gmax) * (1 + 0.012 * min(masa, 10))
        gaji = int(round(UMK[lokasi] * max(mult, 1.0), -4))

        lembur = int(min(72, RNG.gamma(2.0, lem / 2.0)))                      # jam/bulan, maks 72
        shift_malam = int(RNG.random() < night)
        median_tempuh = 35 if lokasi in JABODETABEK else 25                    # Survei Komuter BPS 2023 ~31 mnt
        tempuh = int(np.clip(RNG.lognormal(np.log(median_tempuh), 0.5), 5, 150))
        promosi = round(min(masa, float(RNG.gamma(1.6, 1.4))), 1) if level == 'Staf' else round(min(masa, float(RNG.gamma(1.5, 1.2))), 1)
        pelatihan = int(min(8, RNG.poisson(3.0 if unit == 'Kantor Pusat' else 1.8)))
        kenaikan = round(float(np.clip(RNG.normal(6.0, 2.0), 0, 15)), 1)      # % kenaikan gaji terakhir (UMK 2026 naik ~5-7%)
        kinerja = int(pick([1, 2, 3, 4, 5], [.03, .12, .50, .27, .08], 1)[0])

        rasio = gaji / UMK[lokasi]
        # survei engagement (1-4): dipengaruhi beban kerja, gaji, perjalanan
        def survey(base):
            return int(np.clip(round(base + RNG.normal(0, 0.75)), 1, 4))
        puas_kerja = survey(2.9 - 0.012 * (lembur - 20) + 0.6 * np.log(rasio) - 0.15 * shift_malam)
        atasan = survey(2.9 + RNG.normal(0, 0.3))
        wlb = survey(3.0 - 0.020 * (lembur - 20) - 0.006 * (tempuh - 30) - 0.35 * shift_malam)

        # ---- logit resign sukarela (pola dari studi turnover ritel Indonesia) ----
        z = (-2.20 + off
             + 0.030 * (lembur - 20)
             + 0.30 * shift_malam
             + 0.011 * (tempuh - 30)
             - 1.4 * np.log(rasio)
             + (0.85 if masa < 1 else 0.30 if masa < 2 else 0.0)
             + {'PKWTT (tetap)': 0.0, 'PKWT (kontrak)': 0.35, 'Outsourcing': 0.55}[status]
             + (0.80 if status == 'PKWT (kontrak)' and sisa_kontrak <= 2 else 0.0)
             + 0.17 * max(0.0, promosi - 2)
             - 0.10 * pelatihan
             - 0.40 * (puas_kerja - 2.5) - 0.50 * (atasan - 2.5) - 0.30 * (wlb - 2.5)
             - 0.05 * (kenaikan - 6)
             + (0.30 if kinerja == 5 else 0.0)
             + RNG.normal(0, 0.35))                                          # faktor tak teramati
        p = 1 / (1 + np.exp(-z))
        rows.append(dict(
            jabatan=j, unit=unit, level=level, lokasi=lokasi, status_kerja=status,
            sisa_kontrak_bulan=sisa_kontrak, masa_kerja_tahun=masa, gaji_pokok=gaji,
            umk_lokasi=UMK[lokasi], rasio_gaji_umk=round(rasio, 3), kenaikan_gaji_terakhir_pct=kenaikan,
            lembur_jam_per_bulan=lembur, shift_malam=shift_malam, waktu_tempuh_menit=tempuh,
            tahun_sejak_promosi=promosi, pelatihan_per_tahun=pelatihan, nilai_kinerja=kinerja,
            kepuasan_kerja=puas_kerja, hubungan_atasan=atasan, work_life_balance=wlb,
            resign=int(RNG.random() < p),
        ))
    df = pd.DataFrame(rows)
    # survei engagement tidak diisi semua karyawan (~6% kosong) -> realistis, perlu imputasi
    for c in ['kepuasan_kerja', 'hubungan_atasan', 'work_life_balance']:
        df.loc[RNG.random(len(df)) < 0.06, c] = np.nan
    df.insert(0, 'id_karyawan', [f'KR{10001 + i}' for i in range(len(df))])
    return df


if __name__ == '__main__':
    df = generate()
    df.to_csv('data/karyawan_ritel_2026.csv', index=False)
    print(df.shape, f"resign rate {df.resign.mean():.1%}")
    print(df.groupby('unit').resign.mean().round(3).to_dict())
    print(df.groupby('status_kerja').resign.mean().round(3).to_dict())
