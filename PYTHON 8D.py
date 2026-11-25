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


