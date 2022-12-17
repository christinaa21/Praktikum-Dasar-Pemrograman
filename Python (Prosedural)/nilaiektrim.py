# NILAI EKSTRIM
# Membuat program yang membaca sebuah integer N (asumsikan 0 < N <= 100), lalu membaca N buah
# integer dan menyimpan setiap integer ke dalam suatu array. Selanjutnya, program menerima masukan
# sebuah nilai integer, misalnya X, dan menampilkan:
# - Jika X ada di array, apakah X adalah nilai maksimum (tuliskan “maksimum”) atau nilai minimum
# (tuliskan “minimum”) atau keduanya. Jika bukan nilai maksimum atau minimum, menuliskan “N#A”.
# - Jika X tidak ada di array, tuliskan “X tidak ada”. 

# KAMUS
# N, X, i, max, min = int
# list_N = list
# ada = bool

# ALGORITMA
N = int(input())
list_N = [0 for i in range(N)]
for i in range(N):
    list_N[i] = int(input())

max = list_N[0]
min = list_N[0]
for i in list_N:
    if i >= max:
        max = i
    elif i <= min:
        min = i

X = int(input())
ada = False
for i in list_N:
    if i == X:
        ada = True
        if (X == max):
            print("maksimum")
        if (X == min):
            print("minimum")
        if (X != max) and (X != min):
            print("N#A")
        break
if ada == False:
    print(X, "tidak ada")