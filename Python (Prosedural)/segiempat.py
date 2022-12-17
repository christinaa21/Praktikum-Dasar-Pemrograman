# SEGI EMPAT
# Membuat program yang membaca N (sebuah integer) berikut C1 dan C2 (dua buah karakter),
# dan kemudian menuliskan bentuk segi empat dengan syarat N>0 dan C1 tidak sama dengan C2.
# Jika syarat tidak dipenuhi, diberikan pesan kesalahan.

# KAMUS
# N, i = int
# C1, C2 = str

# ALGORITMA
N = int(input())
C1 = str(input()[0])
C2 = str(input()[0])

if N > 0 and C1 != C2:
    for i in range(N):
        if i == 0 or i == N-1:
            print(N*C1)
        else:
            print(C1 + (N-2)*C2 + C1)
else:
    print("Masukan tidak valid")