import utils

def analisis_teks(teks):
    if teks.strip() == "":
        jumlah_baris = 0
    else:
        baris = teks.split('\n')
        jumlah_baris = len(baris)

    jumlah_vokal = 0
    jumlah_konsonan = 0
    
    for huruf in teks:
        if utils.cek_vokal(huruf):
            jumlah_vokal += 1
        elif utils.cek_konsonan(huruf):
            jumlah_konsonan += 1

    kata_mentah = teks.split()
    jumlah_kata = len(kata_mentah)

    kamus_kata = {}
    for kata in kata_mentah:
        kata_bersih = utils.bersihkan_kata(kata)
        if kata_bersih != "":
            if kata_bersih in kamus_kata:
                kamus_kata[kata_bersih] += 1
            else:
                kamus_kata[kata_bersih] = 1

    frekuensi_terurut = sorted(kamus_kata.items(), key=lambda x: x[1], reverse=True)
    
    top_5 = frekuensi_terurut[:5]

    return {
        "jumlah_baris": jumlah_baris,
        "jumlah_kata": jumlah_kata,
        "jumlah_vokal": jumlah_vokal,
        "jumlah_konsonan": jumlah_konsonan,
        "top_5": top_5
    }