def bersihkan_kata(kata):
    kata_bersih = ""
    for huruf in kata:
        if huruf.isalpha():
            kata_bersih += huruf
    return kata_bersih.lower()

def cek_vokal(huruf):
    huruf = huruf.lower()
    if huruf in "aiueo":
        return True
    else:
        return False

def cek_konsonan(huruf):
    if huruf.isalpha() and not cek_vokal(huruf):
        return True
    else:
        return False