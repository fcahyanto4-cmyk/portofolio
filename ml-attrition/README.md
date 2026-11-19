# Prediksi Karyawan Resign (Employee Attrition)

Proyek machine learning untuk memprediksi risiko karyawan resign dan menjelaskan faktor kerja yang mendorongnya.

- **Showcase & simulator interaktif:** [`hr-attrition.html`](../hr-attrition.html)
- **Notebook (Bahasa Indonesia):** [`hr_attrition_prediction.ipynb`](hr_attrition_prediction.ipynb)
- **Model untuk web:** [`attrition_model.json`](attrition_model.json) — koefisien + parameter preprocessing; skor di browser identik dengan scikit-learn
- **Data:** [`data/ibm_hr_attrition.csv`](data/ibm_hr_attrition.csv) — IBM HR Analytics Employee Attrition (dataset fiktif, 1.470 karyawan)

## Ringkasan hasil

| | |
|---|---|
| Model | Logistic Regression (scikit-learn Pipeline) |
| Fitur | 18 faktor kerja; tanpa gender, status pernikahan, usia |
| CV ROC-AUC (5-fold) | 0,855 |
| Test ROC-AUC | 0,836 |
| Test recall / precision (ambang 0,18, F2) | 74,5% / 38,5% |
| Fokus ke 20% karyawan berisiko tertinggi | menangkap 68% yang resign |

Faktor pendorong terbesar: lembur, sering dinas luar, peran sales, job level 1, dan tidak adanya opsi saham.
Faktor penahan: opsi saham, total pengalaman kerja, gaji, kepuasan lingkungan & pekerjaan, lama bersama atasan.

## Menjalankan ulang

```bash
pip install pandas scikit-learn matplotlib jupyter
cd ml-attrition
jupyter notebook hr_attrition_prediction.ipynb
```
