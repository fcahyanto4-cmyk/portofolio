# Kajian Prediktif Risiko Resign Karyawan Ritel Modern (Konteks Indonesia)

Proyek machine learning untuk memprediksi risiko karyawan resign di jaringan ritel modern Indonesia dan menjelaskan faktor kerja yang mendorongnya.

> **Catatan metodologi data.** Data karyawan perusahaan bersifat rahasia, sehingga kajian ini memakai data simulasi dari [`generate_data.py`](generate_data.py) yang dikalibrasi dengan sumber Indonesia: UMK 2026, PP 35/2021 (batas lembur & PKWT), Survei Komuter Jabodetabek BPS 2023, dan studi turnover ritel Indonesia. Daftar sumber lengkap ada di aplikasi (menu *Tentang Data*).

- **Aplikasi web TalentPulse (7 modul):** [`hr-attrition.html`](../hr-attrition.html)
- **Notebook (Bahasa Indonesia):** [`prediksi_resign_karyawan_ritel.ipynb`](prediksi_resign_karyawan_ritel.ipynb)
- **Generator data terkalibrasi:** [`generate_data.py`](generate_data.py)
- **Data:** [`data/karyawan_ritel_2026.csv`](data/karyawan_ritel_2026.csv) — 2.400 karyawan, 11 jabatan, 7 kota
- **Model untuk web:** [`attrition_model.json`](attrition_model.json) — skor di browser identik dengan scikit-learn

## Ringkasan hasil

| | |
|---|---|
| Model | Logistic Regression (scikit-learn Pipeline, imputasi median) |
| Fitur | Rasio gaji ÷ UMK, status PKWT/outsourcing, kontrak habis ≤2 bulan, lembur, shift malam, waktu tempuh, masa kerja, promosi, pelatihan, survei engagement |
| Tidak dipakai | Gender, usia, status pernikahan, agama, suku, lokasi |
| CV ROC-AUC (5-fold) | 0,779 |
| Test ROC-AUC | 0,763 |
| Ambang (F1) | 0,21 → recall 67%, precision 40% |
| Fokus ke 30% karyawan berisiko tertinggi | menangkap 61% yang resign |

## Menjalankan ulang

```bash
pip install pandas scikit-learn matplotlib jupyter
cd ml-attrition
python generate_data.py          # opsional: buat ulang data sintetis
jupyter notebook prediksi_resign_karyawan_ritel.ipynb
```
