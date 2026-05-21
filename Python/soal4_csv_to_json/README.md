# UTS PEMROGRAMAN DASAR
## Konversi Data CSV ke JSON (Python)

### Nama
[APRILLIA NUR HASNI]

### NIM
[2025806071]

---

# Penjelasan Singkat Program

## 1. convert.py
File utama program yang berfungsi untuk:
- Membaca file CSV hasil program C
- Menampilkan data mahasiswa dengan rapi
- Menghitung rata-rata nilai akhir mahasiswa
- Mengonversi data ke format JSON
- Menyimpan hasil konversi ke file JSON

---

## 2. data_mahasiswa.csv
File input hasil dari program C pada soal 1 yang berisi data mahasiswa seperti:
- Nama
- NIM
- Nilai Tugas
- Nilai UTS
- Nilai UAS
- Nilai Akhir
- Mutu

---

## 3. data_mahasiswa.json
File hasil konversi dari format CSV ke JSON yang digunakan untuk pertukaran data antar sistem.

---

# Fitur Program

- Membaca file CSV
- Menampilkan data mahasiswa dengan format tabel
- Menghitung rata-rata nilai akhir
- Konversi otomatis CSV ke JSON
- Penyimpanan data JSON
- Error handling file
- Format output rapi dan mudah dibaca

---

# Struktur Project

```plaintext
soal4_csv_to_json/
├── convert.py
├── data_mahasiswa.csv
├── data_mahasiswa.json
└── README.md
```

---

# Struktur Data Mahasiswa

## Data yang Digunakan
- Nama
- NIM
- Nilai Tugas
- Nilai UTS
- Nilai UAS
- Nilai Akhir
- Mutu

---

# Rumus Nilai Akhir

```text
Nilai Akhir =
(30% × Tugas) +
(30% × UTS) +
(40% × UAS)
```

---

# Kriteria Mutu

```text
A : >= 85
B : >= 70
C : >= 55
D : >= 40
E : < 40
```

---

# Contoh Isi CSV

```csv
Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu
april,2025806071,80.0,90.0,100.0,91.0,A
adillah,2025806075,70.0,80.0,90.0,81.0,B
salsabila,2025806068,100.0,75.0,80.0,84.5,B

---

# Contoh Hasil JSON

```json

[
    {
        "name": "april",
        "score": 10
    },
    {
        "name": "salsabila",
        "score": 90
    },
    {
        "name": "isma",
        "score": 10
    },
    {
        "name": "adillah",
        "score": 10
    },
    {
        "name": "dinda",
        "score": 40
    }
]

---

# Cara Running Program

## 1. Pastikan File Sudah Lengkap

Pastikan folder project berisi file berikut:

```plaintext
soal4_csv_to_json/
├── convert.py
├── data_mahasiswa.csv
└── README.md
```

---

## 2. Jalankan Program C Terlebih Dahulu

Pada program C soal 1:
- Tambahkan data mahasiswa
- Pilih menu:

```text
5. Simpan CSV
```

Program C akan otomatis membuat file:

```plaintext
data_mahasiswa.csv
```

---

## 3. Pindahkan File CSV

Copy file:

```plaintext
data_mahasiswa.csv
```

ke folder:

```plaintext
soal4_csv_to_json/
```

---

## 4. Buka Terminal / CMD

Masuk ke folder project:

```bash
cd soal4_csv_to_json
```

---

## 5. Jalankan Program Python

```bash
python convert.py
```

atau jika menggunakan Python3:

```bash
python3 convert.py
```

---

## 6. Hasil Program

Program akan:
- Membaca data dari file CSV
- Menampilkan data mahasiswa
- Menghitung rata-rata nilai akhir
- Membuat file JSON otomatis

---

## 7. File JSON Akan Muncul

Setelah program berhasil dijalankan, otomatis akan muncul file:

```plaintext
data_mahasiswa.json
```

di dalam folder project.

---

# Contoh Tampilan Program

```text
==============================================================
               DATA MAHASISWA
==============================================================

Nama: april | NIM: 2025806071 | Nilai: 80.0 | Mutu: 90.0

Nama: adillah | NIM: 2025806075 | Nilai: 70.0 Mutu: 80.0

Nama: salsa | NIM: 2025806068 | Nilai: 100.0 | Mutu: 75.0
==============================================================

Rata-rata Nilai Akhir : 83.33

Data berhasil dikonversi ke data_mahasiswa.json
```

---

# Screenshot Program

## Screenshot Struktur Folder

![Struktur Folder](https://cdn.phototourl.com/free/2026-05-21-a13fab2d-f02b-472e-b561-1290cb9096e6.jpg)

---

## Screenshot Program Berjalan

![Program Running](https://cdn.phototourl.com/free/2026-05-21-5a0ef96a-22a6-4bd6-a8a0-9ddd74fed330.jpg)

---

## Screenshot File JSON

![JSON Result](https://cdn.phototourl.com/free/2026-05-21-4198836a-f9fa-4c0a-9917-c96b6c9d16ec.jpg)

---

# Studi Kasus

Program ini mensimulasikan proses pertukaran data antar sistem akademik menggunakan format berbeda, yaitu:

```text
CSV ↔ JSON
```

Konsep ini banyak digunakan pada:
- Sistem akademik
- Database
- API
- Web service
- Integrasi antar aplikasi

---

# Kesimpulan

Program berhasil:
- Membaca data dari file CSV
- Mengolah dan menampilkan data mahasiswa
- Menghitung rata-rata nilai akhir
- Mengonversi data ke format JSON
- Menyimpan hasil konversi secara otomatis

Program dibuat menggunakan bahasa Python dan terintegrasi dengan program C dari soal 1.