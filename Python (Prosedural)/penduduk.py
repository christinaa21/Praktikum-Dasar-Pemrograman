# PENDUDUK
# Membuat program yang digunakan untuk membaca masukan jumlah penduduk desa dari
# sebuah kecamatan di suatu kota. Program pertama-tama akan membaca input N yang
# merupakan jumlah desa dalam kecamatan. N diasumsikan selalu valid. Selanjutnya,
# program akan meminta input jumlah penduduk setiap desa sebanyak N (input jumlah
# penduduk desa dianggap selalu valid, yaitu > 0) dan menghitung jumlah penduduk
# kecamatan (total penduduk desa).

# KAMUS
# N, sum, penduduk, i = int

# ALGORITMA
N = int(input())
sum = 0
for i in range(N):
    penduduk = int(input())
    sum += penduduk
print(sum)