#melakukan impor library datetime untuk mendapatkan waktu sekarang
from datetime import datetime

#menuliskan informasi yang akan ditampilkan dalam bentuk variabel
nama = "Ervizal Buana Jatiputra"
nama_panggilan = "Vizal."
jenis_kelamin = "laki-laki"
sekarang = datetime.now()
tanggal_sekarang = sekarang.day
bulan_sekarang = sekarang.month
tahun_sekarang = sekarang.year
tanggal_lahir = 3
bulan_lahir = 7
tahun_lahir = 2002
berat_badan = 57.7
tinggi_badan = 172.6
golongan_darah = "B"
ukuran_sepatu = 43
alamat_rumah = "Jl. Soekarno-Hatta No. 37, Kota Probolinggo."
tempat_lahir = "Jember"
tanggallahir = 3
bulanlahir = "Juli"
tahunlahir = 2002
hobi = "programming, bermain gitar, renang, basket, memanah, nonton drakor"
skill = "public speaking dan programming"
pekerjaan = "mahasiswa"
jurusan = "S-1 Teknik Industri"
fakultas = "Fakultas Teknik"
Angkatan = 2020
universitas = "Universitas Sebelas Maret"

#operasi menghitung umur secara detail
sekarang = int(tanggal_sekarang) + (int(bulan_sekarang)*30) + (int(tahun_sekarang)*365)
lahir = int(tanggal_lahir) + (int(bulan_lahir)*30) + (int(tahun_lahir)*365)
tahun = int((sekarang - lahir) / 365)
bulan = int(((sekarang - lahir)%365) / 30)
hari = int(((sekarang - lahir)%365) % 30)

# Menampilkan variabel yang telah ditulis
print("======================================")
print("=========== Identitas Diri ===========")
print("======================================")
print("Halo! perkenalkan namaku", nama, "dan", "biasa dipanggil", nama_panggilan, "Jenis kelaminku", jenis_kelamin," dan umurku", tahun, "Tahun", bulan, "Bulan", hari, "Hari", "\n", "berat badanku", berat_badan, "Kg", "\n", "Tinggi badanku", "Cm", tinggi_badan, "\n", "Golongan darahku", golongan_darah, "\n", "Ukuran sepatuku", ukuran_sepatu, "\n")
print("Aku tinggal di", alamat_rumah, "aku lahir di", tempat_lahir, "pada", tanggallahir, bulanlahir, tahunlahir, "\n", "Hobiku adalah", hobi, "Aku memiliki kemampuan dalam", skill, "\n", "Saat ini aku adalah seorang", pekerjaan, "di", jurusan, fakultas, universitas, "Angkatan", Angkatan, "dan aku bangga sekali menjadi mahasiswa disini", "\n")
print("Terima kasih telah menjalankan program ini, salam kenal pembaca!:)")
print("======================================")
