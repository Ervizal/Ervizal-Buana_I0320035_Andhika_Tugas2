print("=====================================================")
print("====== Program Menghitung Luas Persegi Panjang ======")
print("=====================================================")
panjang = float(input("Masukkan panjang"))
lebar = float(input("Masukkan lebar"))
luas = panjang*lebar
print("Luas persegi panjang adalah", luas, "satuan")

import math
print("===================================================")
print("======== Program Menghitung Luas Lingkaran ========")
print("===================================================")
menu = int(input("Diketahui (1)jari-jari atau (2)diameter tuliskan angkanya"))
if(menu == 1):
	r = float(input("Masukkan jari-jari"))
	luas = math.pi*(math.pow(r,2))
	print("Luas lingkaran adalah", luas, "Satuan")
elif(menu == 2):
	d = float (input("Masukkan diameter"))
	d /= 2
	luas = math.pi*(math.pow(d,2))
	print("Luas lingkaran adalah", luas, "Satuan")
else:
    print("input salah")

import math
print("===================================================")
print("===== Program Menghitung Luas Permukaan Kubus =====")
print("===================================================")
sisi = float(input("Masukkan panjang sisi kubus"))
luas_permukaan = 6*(math.pow(sisi,2))
print("Luas permukaan kubus adalah", luas_permukaan, "Satuan")

print("====================================================")
print("==== Program Konversi Suhu Celcius ke Farenheit ====")
print("====================================================")
celcius = float(input("Masukkan suhu dalam celcius"))
konstanta = 9/5
farenheit = (konstanta*celcius)+32
print("Suhu dalam farenheit adalah", farenheit, "Farenheit")

print("====================================================")
print("====== Program Konversi Suhu Reamur ke Kelvin ======")
print("====================================================")
reamur = float(input("Masukkan suhu dalam Reamur"))
konstanta = 5/4
kelvin = (konstanta*reamur)+273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")