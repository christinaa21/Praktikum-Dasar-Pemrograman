# LINGKARAN
# Membuat program yang digunakan untuk menghitung luas lingkaran.
# Program menerima input jari-jari (integer). Input jari-jari harus
# divalidasi sehingga selalu > 0. Apabila jari-jari yang dimasukkan <= 0,
# program akan mengeluarkan pesan error. Jika jari-jari yang dimasukkan valid,
# program menghasilkan luas lingkaran dengan rumus: 3.1415 * jari-jari * jari-jari.

# KAMUS
# r = int

# ALGORITMA
r = int(input())
if r <= 0:
    print("Jari-jari harus > 0")
else:
    print("%.2f" % (3.1415 * r * r))