# Prediksi Pelanggan Churn — PT NusaNet Digital (Internet Rumah, Konteks Indonesia)

Proyek machine learning untuk memprediksi pelanggan internet rumah yang akan berhenti berlangganan dalam 6 bulan, menghitung pendapatan berisiko dalam Rupiah, dan mensimulasikan ROI kampanye retensi.

> **Data sintetis.** PT NusaNet Digital adalah ISP fiktif. Data dibuat dengan [`generate_data.py`](generate_data.py), yang parameternya dikalibrasi dengan kondisi pasar fixed broadband Indonesia 2025–2026: ARPU IndiHome, harga paket 2026, munculnya paket 100 Mbps Rp100 ribu, data kecepatan internet, penetrasi bundling seluler, dan survei loyalitas APJII. Daftar sumber lengkap ada di halaman aplikasi (menu *Tentang Data*).

- **Aplikasi web (7 modul):** [`churn-isp.html`](../churn-isp.html)
- **Notebook (Bahasa Indonesia):** [`prediksi_churn_nusanet.ipynb`](prediksi_churn_nusanet.ipynb)
- **Generator data terkalibrasi:** [`generate_data.py`](generate_data.py)
- **Data:** [`data/nusanet_pelanggan_2026.csv`](data/nusanet_pelanggan_2026.csv) — 3.000 pelanggan, 7 kota, 5 paket
- **Model untuk web:** [`churn_model.json`](churn_model.json) — skor di browser identik dengan scikit-learn

## Ringkasan hasil

| | |
|---|---|
| Model | Logistic Regression (scikit-learn Pipeline, imputasi median) |
| Fitur | Gangguan, lama perbaikan, kecepatan aktual vs paket, keluhan CS, telat bayar, isolir, kepuasan, harga per Mbps, pemakaian data, add-on TV, bundling seluler, promo berakhir, kompetitor Rp100rb di area, kontrak & sisa kontrak, metode bayar, lama langganan |
| CV ROC-AUC (5-fold) | 0,811 |
| Test ROC-AUC | 0,783 |
| Fokus ke 30% pelanggan berisiko tertinggi | menangkap 63% yang churn |
| Pendapatan berisiko | ~Rp1,38 miliar per tahun (15,2% pendapatan) |

## Menjalankan ulang

```bash
pip install pandas scikit-learn matplotlib jupyter
cd ml-churn
python generate_data.py          # opsional: buat ulang data sintetis
jupyter notebook prediksi_churn_nusanet.ipynb
```
