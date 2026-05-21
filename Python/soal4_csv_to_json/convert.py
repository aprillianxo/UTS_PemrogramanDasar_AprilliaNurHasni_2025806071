import json
import os
import argparse

def proses_baris_csv(baris_csv):
    data_mahasiswa = []
    mulai_index = 1 if "nama" in baris_csv[0].lower() else 0
    
    for i in range(mulai_index, len(baris_csv)):
        baris = baris_csv[i].strip()
        if baris == "":
            continue
            
        kolom = baris.split(",")
        nama = kolom[0].strip()
        nim = kolom[1].strip()
        nilai_akhir = float(kolom[2].strip())
        mutu = kolom[3].strip()

        mahasiswa = {
            "nama": nama,
            "nim": nim,
            "nilai_akhir": nilai_akhir,
            "mutu": mutu
        }
        data_mahasiswa.append(mahasiswa)
        
    return data_mahasiswa

def hitung_rata_rata(data_mahasiswa):
    if len(data_mahasiswa) == 0:
        return 0.0
        
    total_nilai = 0.0
    for mhs in data_mahasiswa:
        total_nilai += mhs["nilai_akhir"]
        
    return total_nilai / len(data_mahasiswa)

def test_hitung_rata_rata():
    data_dummy = [
        {"nama": "Andi", "nim": "1", "nilai_akhir": 80.0, "mutu": "A"},
        {"nama": "Budi", "nim": "2", "nilai_akhir": 70.0, "mutu": "B"}
    ]
    hasil = hitung_rata_rata(data_dummy)
    assert hasil == 75.0
    
    data_kosong = []
    hasil_kosong = hitung_rata_rata(data_kosong)
    assert hasil_kosong == 0.0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    nama_file_input = args.file

    if not os.path.exists(nama_file_input):
        print(f"File '{nama_file_input}' tidak ditemukan!")
        return

    file_csv = open(nama_file_input, "r", encoding="utf-8")
    baris_csv = file_csv.readlines()
    file_csv.close()

    data_mahasiswa = proses_baris_csv(baris_csv)

    print("=== DATA MAHASISWA ===")
    for mhs in data_mahasiswa:
        print(f"Nama: {mhs['nama'].ljust(10)} | NIM: {mhs['nim']} | Nilai: {mhs['nilai_akhir']} | Mutu: {mhs['mutu']}")

    rata_rata = hitung_rata_rata(data_mahasiswa)

    print("\n=== STATISTIK ===")
    print(f"Rata-rata Nilai Akhir: {rata_rata:.2f}")

    nama_file_output = nama_file_input.replace(".csv", ".json")
    file_json = open(nama_file_output, "w", encoding="utf-8")
    json.dump(data_mahasiswa, file_json, indent=4)
    file_json.close()

    print(f"\n[SUKSES] Data dikonversi dan disimpan ke '{nama_file_output}'")

if __name__ == "__main__":
    main()