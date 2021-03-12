print("=====================================================")
print("====== Program Menghitung Luas Persegi Panjang ======") 					#menuliskan judul program
print("=====================================================")
panjang = float(input("Masukkan panjang"))										#menyimpan input panjang di variabel panjang
lebar = float(input("Masukkan lebar"))											#menyimpan input lebar di variabel lebar
luas = panjang*lebar															#operasi hitung luas persegi panjang
print("Luas persegi panjang adalah", luas, "satuan")							#mengeluarkan output hasil perhitungan

import math																		#mengimpor library math
print("===================================================")
print("======== Program Menghitung Luas Lingkaran ========")					#menuliskan judul program
print("===================================================")
menu = int(input("Diketahui (1)jari-jari atau (2)diameter tuliskan angkanya"))	#membuat menu untuk menentukan input
if(menu == 1):																	#percabangan pertama apabila input jari-jari
	r = float(input("Masukkan jari-jari"))										#menyimpan input jari-jari dalam variabel r
	luas = math.pi*(math.pow(r,2))												#operasi menghitung luas lingkaran
	print("Luas lingkaran adalah", luas, "Satuan")								#mengeluarkan output hasil perhitungan
elif(menu == 2):																#percabangan kedua apabila input diameter
	d = float (input("Masukkan diameter"))										#menyimpan input diameter dalam variabel d
	d /= 2
	luas = math.pi*(math.pow(d,2))												#operasi menghitung luas lingkaran
	print("Luas lingkaran adalah", luas, "Satuan")								#mengeluarkan output hasil perhitungan
else:
    print("input salah")														#output apabila input yang dmasukkan tidak sesuai

import math																		#mengimpor library math
print("===================================================")
print("===== Program Menghitung Luas Permukaan Kubus =====")					#menuliskan judul program
print("===================================================")
sisi = float(input("Masukkan panjang sisi kubus"))								#menyimpan input dalam variabel sisi
luas_permukaan = 6*(math.pow(sisi,2))											#operasi hitung luas permukaan
print("Luas permukaan kubus adalah", luas_permukaan, "Satuan")					#menampilkan output hasil perhitungan

print("====================================================")
print("==== Program Konversi Suhu Celcius ke Farenheit ====")					#menuliskan judul program
print("====================================================")
celcius = float(input("Masukkan suhu dalam celcius"))							#menyimpan input suhu berderajat celcius dalam variabel celcius
konstanta = 9/5																	#membuat konstanta rumus konversi
farenheit = (konstanta*celcius)+32												#operasi mengkonversi celsius ke farenheit
print("Suhu dalam farenheit adalah", farenheit, "Farenheit")					#menampilkan output hasil konversi

print("====================================================")
print("====== Program Konversi Suhu Reamur ke Kelvin ======")					#menuliskan judul program
print("====================================================")
reamur = float(input("Masukkan suhu dalam Reamur"))								#menyimpat input suhu berderajat reamur dalam variabel reamur
konstanta = 5/4																	#membuat konstanta rumus konversi
kelvin = (konstanta*reamur)+273													#operasi mengkonversi reamur ke kelvin
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")								#menampilkan output hasil konversi