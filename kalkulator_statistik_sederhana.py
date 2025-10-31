daftar_angka = input("Masukkan daftar angka bilangan bulat (pisahkan dengan koma): ")
daftar_angka = [int(angka) for angka in daftar_angka.split(',')]

def mean(daftar_angka):
    return float(sum(daftar_angka) / len(daftar_angka))

def maksimum(daftar_angka):
    return max(daftar_angka)

def minimum(daftar_angka):
    return min(daftar_angka)

def jumlah_angka(daftar_angka):
    return len(daftar_angka)

def angka_genap(daftar_angka):
    return len([angka for angka in daftar_angka if angka % 2 == 0])

def angka_ganjil(daftar_angka):
    return len([angka for angka in daftar_angka if angka % 2 != 0])

print("\n Rata-rata     : " + str(mean(daftar_angka)))
print(" Maksimum      : " + str(maksimum(daftar_angka)))
print(" Minimum       : " + str(minimum(daftar_angka)))
print(" Jumlah angka  : " + str(jumlah_angka(daftar_angka)))
print(" Angka genap   : " + str(angka_genap(daftar_angka)))
print(" Angka ganjil  : " + str(angka_ganjil(daftar_angka)))
