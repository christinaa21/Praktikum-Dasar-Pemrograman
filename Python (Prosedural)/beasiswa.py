# BEASISWA
# Membuat program yang membaca input 2 buah bilangan riil (float), misalnya ip dan pot,
# dengan ip mewakili IP mahasiswa (bernilai 0..4) dan pot mewakili pendapatan orang tua
# (dalam juta rupiah, bernilai >= 0) dan menuliskan ke layar kategori beasiswa (bernilai 0..4)
# yang berhak didapatkan oleh mahasiswa tersebut sesuai ketentuan di atas (jika kategori 0,
# berarti mahasiswa tersebut tidak berhak atas beasiswa).

# KAMUS
# ip, pot = float

# ALGORITMA
ip = float(input())
pot = float(input())
if ip >= 3.5:
    print(4)
elif pot < 1 and ip < 3.5:
    print(1)
elif 1 <= pot < 5 and 2 <= ip < 3.5:
    print(3)
elif 1 <= pot < 5 and ip < 2:
    print(2)
else:
    print(0)