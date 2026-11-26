print("="*150)
print()
print("MINI PROJECT".center(150))
print("PROGRAM KOMPUTER".center(150))
print()
print("ANALISIS DAN REKOMENDASI WISATA JEMBER")
print("_"*150)
print()
print()
print("DISUSUN OLEH : ".center(150))
print()
print("KELOMPOK 8D".center(150))
print()
print()
print("TSANI ROSYIDAH BASYUSYI          (2610932007)".center(145) + " ".center(5))
print("KUNTUM KHAIRANI                  (2610933017)".center(145) + " ".center(5))
print("MUHAMMMAD MUKDIARAFFI FADILLAH   (2610933029)".center(145) + " ".center(5))
print("MUHAMMAD FADLI                   (2610932011)".center(145) + " ".center(5))
print(" ".center(150))
print()
print()
print("ASISTEN PEMBIMBING : ".center(150))
print()
print("JIHAN FITRI SAKINAH".center(150))
print(" ".center(150))
print(" ".center(150))
print()
print("LABORATORIUM SISTEM INFORMASI DAN KOMPUTASI".center(150))
print("JURUSAN TEKNIK INDUSTRI".center(150))
print("FAKULTAS TEKNIK".center(150))
print("UNIVERSITAS ANDALAS".center(150))
print("2026".center(150))
print()
print("="*150)
print()
print("SELAMAT DATANG DI".center(150))
print("PROGRAM ANALISIS DAN REKOMENDASI DESTINASI WISATA JEMBER BERDASARKAN RATING DAN HARGA TIKET".center(150))
print()
print()
print("SILAHKAN PILIH BEBERAPA MENU BERIKUT : ")

import csv

nama_file = r"dataset_wisata_jember.csv"

def baca_dataset():
    data_wisata = []

    try:
        with open(nama_file, "r", encoding="utf-8-sig", newline="") as file:
            pembaca = csv.DictReader(file)

            for baris in pembaca:
                data_wisata.append(baris)

        return data_wisata

    except FileNotFoundError:
        print("File dataset tidak ditemukan")
        return []


def ubah_harga(harga):
    harga = str(harga).strip().lower()

    if harga in ["gratis"]:
        return 0

    angka = "".join(char for char in harga if char.isdigit())

    if angka == "":
        return 0

    return int(angka)

def pilih_hari ():
    while True:
        print("\nPilih Jenis Kunjungan")
        print("1. Weekday")
        print("2. Weekend")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            return "Tiket Masuk Weekday"

        elif pilihan == "2":
            return "Tiket Masuk Weekend"

        else:
            print("Pilihan tidak valid!")

def daftar_harga(data_wisata, kolom_harga):
    daftar = set()

    for wisata in data_wisata:
        harga = ubah_harga(wisata[kolom_harga])

    print("\nDaftar Harga Tiket:")

    for harga in sorted(daftar):
        print(f"Rp{harga:,}".replace(",", "."))

def rekomendasi_harga(data_wisata):
    kolom_harga = pilih_hari()
    daftar_harga(data_wisata, kolom_harga)

    while True:
        input_harga = input("\nMasukkan harga tiket yang dicari : ")

        if input_harga.strip().lower() not in ["gartis", "free", "_"]:
            if not any(char.isdigit() for char in input_harga):
                print("MASUKKAN NOMINAL HARGA YANNG BENAR!")
                continue
                
        harga_dicari = ubah_harga(input_harga)
        break

    hasil = []

    for wisata in data_wisata:
        harga = ubah_harga(wisata[kolom_harga])

        if harga == harga_dicari:
            hasil.append(wisata)

    print("\nHasil Rekomendasi Berdasarkan Harga")

    if len(hasil) == 0:
        print("Tidak Ditemukan Wisata Dengan Harga Tersebut")
    else:
        for nomor, wisata in enumerate(hasil, start=1):
            print(f"\n{nomor}. {wisata['Nama Wisata']}")
            print(f" Rating : {wisata['Rating']}")
            print(f" Harga : Rp{ubah_harga(wisata[kolom_harga]):,}".replace(",", "."))
            print(f" Lokasi : {wisata['Lokasi']}")