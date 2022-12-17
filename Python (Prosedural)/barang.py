# BARANG
# Membuat program yang membaca masukan harga sejumlah barang yang dibeli di minimarket.
# Program pertama-tama akan membaca input N yang merupakan jumlah barang. N diasumsikan
# selalu valid (N>0). Selanjutnya, program akan meminta input harga barang sebanyak N
# (input harga dianggap selalu valid) dan menghitung jumlah harga barang.

# KAMUS
# N, sum, harga, i = int

# ALGORITMA
N = int(input())
sum = 0
for i in range(N):
    harga = int(input())
    sum += harga
print(sum)