# kartu.py (1/5)
# Isi: membuat dek 46 kartu, mengacak dek, menamai kartu, dan mengambil kartu.
# 46 = 4 warna x (10 angka + 1 kartu +2) + 1 ganti warna + 1 kartu +4
from random import randint

# tuple: isinya tetap dan tidak diubah
WARNA = ("merah", "biru", "kuning", "hijau")

# satu kartu disimpan sebagai dictionary
def buat_kartu(warna, jenis, nilai=0):
    return {"warna": warna, "jenis": jenis, "nilai": nilai}

# membuat 46 kartu, hasilnya berupa list
def buat_dek():
    dek = []
    for warna in WARNA:
        for angka in range(0, 10):
            dek.append(buat_kartu(warna, "angka", angka))
        dek.append(buat_kartu(warna, "+2"))
    dek.append(buat_kartu("hitam", "ganti"))
    dek.append(buat_kartu("hitam", "+4"))
    return dek

# mengacak dek dengan menukar posisi kartu secara acak
def acak_dek(dek):
    for i in range(len(dek)):
        j = randint(0, len(dek) - 1)
        sementara = dek[i]
        dek[i] = dek[j]
        dek[j] = sementara

# mengubah kartu menjadi teks yang mudah dibaca
def nama_kartu(kartu):
    warna = kartu["warna"]
    nilai = kartu["nilai"]
    hasil = ""
    match kartu["jenis"]:
        case "angka":
            hasil = f"{warna} {nilai}"
        case "+2":
            hasil = f"{warna} +2"
        case "ganti":
            hasil = "GANTI WARNA"
        case _:
            hasil = "+4 (hitam)"
    return hasil

# mengambil kartu dari dek, jika dek habis maka buangan dikocok jadi dek baru
def ambil_kartu(dek, buangan, jumlah=1):
    hasil = []
    for i in range(jumlah):
        if len(dek) == 0 and len(buangan) > 1:
            atas = buangan.pop()        # kartu teratas tetap di meja
            dek.extend(buangan)
            buangan.clear()
            buangan.append(atas)
            acak_dek(dek)
        if len(dek) > 0:
            hasil.append(dek.pop())
    return hasil