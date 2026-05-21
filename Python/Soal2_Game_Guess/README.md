# README.md

# UTS PEMROGRAMAN DASAR
## Guess Battle Game (Python)

### Nama
[APRILLIA NUR HASNI]

### NIM
[2025806071]

---

# Penjelasan Singkat Program

## 1. main.py
File utama program yang berisi:
- Tampilan menu utama
- Input nama pemain
- Menjalankan game
- Menampilkan total skor
- Menampilkan top 5 score

---

## 2. game.py
Berisi seluruh logic permainan seperti:
- Sistem multi level
- Random angka
- Validasi input
- Sistem skor
- Loop permainan
- Kondisi menang dan kalah

---

## 3. scoreboard.py
Berisi fungsi untuk:
- Membaca file JSON
- Menyimpan skor pemain
- Mengurutkan skor tertinggi
- Menampilkan top 5 pemain terbaik

---

## 4. scores.json
File penyimpanan data skor pemain dalam format JSON.

---

# Fitur Program

- Multi-player
- Multi-level
- Sistem skor otomatis
- Penyimpanan data JSON
- Top 5 scoreboard
- Error handling
- Warna terminal menggunakan Colorama

---

# Level Permainan

## Level 1
- Range angka: 1 - 10
- Kesempatan: 3 kali

## Level 2
- Range angka: 1 - 50
- Kesempatan: 5 kali

## Level 3
- Range angka: 1 - 100
- Kesempatan: 7 kali

---

# Contoh Hasil Output (Screenshot)

## Screenshot Menu Program

![Menu Program](https://cdn.phototourl.com/free/2026-05-21-6dc2290c-7f33-44ad-aab4-ced1fbd1a617.jpg)

---

## Screenshot Gameplay

![Gameplay](https://cdn.phototourl.com/free/2026-05-21-be8ef7af-07ae-4858-ac17-80c1171a89c4.jpg)

---

## Screenshot Top Score

![Top Score](https://cdn.phototourl.com/free/2026-05-21-e73d9564-cfc7-403b-ad0a-afabd2f01610.jpg)

---

# Instruksi Run Program

## 1. Masuk ke Folder Project

```bash
cd soal2_game_guess
```

---

## 2. Install Library

```bash
pip install colorama
```

---

## 3. Jalankan Program

```bash
python main.py
```

---

# Contoh Tampilan Program

```text
=============================================
        WELCOME TO GUESS BATTLE
=============================================

Masukkan nama pemain: Ridho

=== LEVEL 1 ===
Tebak angka antara 1 - 10
Kesempatan: 3 kali

Masukkan tebakan: 5
Terlalu kecil!

Masukkan tebakan: 8
Tebakan benar!

Skor level: 20
```

---

# Contoh Tampilan Scoreboard

```text
=== TOP 5 SCORE ===

1. salsabila - 90 pts
2. dinda - 40 pts
3. april - 10 pts
4. isma - 10 pts
5. adillah - 10 pts
```