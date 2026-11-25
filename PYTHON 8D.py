import csv

nama_file = r"C:\Users\ACER\Documents\Mini project 8D\dataset_wisata_jember.csv"


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


