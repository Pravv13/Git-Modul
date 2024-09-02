# Hitung luas lingkaran sederhana
def luas_lingkaran():
    print("-----Program hitung luas lingkaran-----")
    r = int(input("Masukkan panjang jari-jari lingkaran: "))
    luas = 3.14*r*r
    print("Luas lingkaran adalah: ", luas)

luas_lingkaran()
print("<<<<<<>>>>>")
# Hitung volume tabung sederhana
def vol_tabung():
    print("-----Program hitung volume tabung-----")
    r = int(input("Masukkan panjang jari-jari lingkaran: "))
    t = int(input("Masukkan tinggi tabung: "))
    vol = 3.14*r*r*t
    print("Volume tabung adalah: ", vol)

vol_tabung()