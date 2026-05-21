import os
import analyzer

def main():
    if not os.path.exists("input.txt"):
        print("File 'input.txt' tidak ditemukan!")
        return
        
    file_masuk = open("input.txt", "r", encoding="utf-8")
    teks = file_masuk.read()
    file_masuk.close()

    hasil = analyzer.analisis_teks(teks)

    daftar_kata = []
    for data in hasil["top_5"]:
        daftar_kata.append(data[0])
    teks_kata = ", ".join(daftar_kata)

    laporan = "=== LAPORAN ANALISIS TEKS ===\n"
    laporan += "Jumlah baris: " + str(hasil["jumlah_baris"]) + "\n"
    laporan += "Jumlah kata: " + str(hasil["jumlah_kata"]) + "\n"
    laporan += "5 kata yang paling sering muncul: " + teks_kata + "\n"
    laporan += "Jumlah huruf vokal: " + str(hasil["jumlah_vokal"]) + "\n"
    laporan += "Jumlah huruf konsonan: " + str(hasil["jumlah_konsonan"]) + "\n\n"
    
    laporan += "=== Grafik Frekuensi Kata ===\n"
    for data in hasil["top_5"]:
        kata = data[0]
        jumlah = data[1]
        grafik = "#" * jumlah
        laporan += kata.ljust(15) + " " + grafik + "\n"

    print(laporan)

    file_keluar = open("report.txt", "w", encoding="utf-8")
    file_keluar.write(laporan)
    file_keluar.close()

if __name__ == "__main__":
    main()