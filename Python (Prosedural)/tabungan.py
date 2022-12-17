# TABUNGAN
# Membuat program yang membaca masukan jumlah tabungan dari sejumlah siswa di suatu kelas. Program pertama-tama akan membaca
# input N yang merupakan jumlah siswa. N diasumsikan selalu valid, yaitu N > 0. Selanjutnya, program akan meminta input nilai
# tabungan sebanyak N (input nilai tabungan dianggap selalu valid, yaitu > 0) dan menghitung jumlah tabungan.

# KAMUS
# N, sum, tabungan, i = int

# ALGORITMA
N = int(input())
sum = 0
for i in range(N):
    tabungan = int(input())
    sum += tabungan
print(sum)