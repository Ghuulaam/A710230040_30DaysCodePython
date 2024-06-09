try:
    angka = int(input("Masukan Angka: "))
    print("Pangkat dua dari dua angka tersebut adalah", angka**2)
except ValueError:
    print("Input Harus Berupa Angka !")