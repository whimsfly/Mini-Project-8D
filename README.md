# MINI-PROJECT-8D

#  Analisis dan Rekomendasi Wisata Jember
Program Python berbasis terminal untuk menganalisis dan merekomendasikan destinasi wisata Kabupaten Jember berdasarkan rating dan harga tiket masuk.
Mini project mata kuliah Pemrograman Komputer, Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas.

#  Tentang Proyek
Proyek ini merupakan program analisis dan rekomendasi destinasi wisata di Kabupaten Jember menggunakan bahasa pemrograman Python dan dataset CSV. Program ini membantu pengguna menemukan destinasi wisata berdasarkan harga tiket serta menentukan 10 destinasi terbaik berdasarkan rating dan harga tiket masuk.

#  Fitur Utama
1. Rekomendasi Berdasarkan Harga
   Mencari destinasi wisata berdasarkan harga tiket masuk weekday atau weekend.

2. Top 10 Destinasi Wisata
   Menampilkan 10 destinasi wisata terbaik dengan bobot rating 70% dan harga tiket 30%.

3. Detail Destinasi Wisata
   Menampilkan informasi nama wisata, rating, harga tiket, lokasi, deskripsi, dan link foto.

   # Dataset
• File : dataset_wisata_jember.csv
• Sumber: dataset pariwisata Jember dari Kaggle, awalnya berupa file Excel yang dikonversi ke CSV.
• Jumlah data: 76 destinasi wisata.
• Kolom: Nama Wisata, Rating, Tiket Masuk Weekday, Tiket Masuk Weekend, Lokasi, Deskripsi, dan Link Foto.

# Struktur File

| File | Isi |
| :--- | :--- |
| `main.py` | Menu utama dan titik awal program |
| `data_wisata.py` | Membaca dataset, mengubah format harga, memilih jenis kunjungan |
| `rekomendasi_harga.py` | Fitur rekomendasi berdasarkan harga (menu 1) |
| `top10.py` | Perhitungan skor dan Top 10 destinasi (menu 2) |
| `destinasi.py` | Daftar destinasi dan detailnya (menu 3) |
| `dataset_wisata_jember.csv` | Dataset destinasi wisata |

# Cara Menjalankan
1. Pastikan Python 3 sudah terpasang.
2. Letakkan semua file .py dan dataset_wisata_jember.csv dalam satu folder.
3. Buka terminal di folder tersebut, lalu jalankan:
python main.py
4. Pilih menu dengan mengetik angka 1 sampai 4.

   
