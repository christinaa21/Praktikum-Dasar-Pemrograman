# Nama: Christina Wijaya
# NIM: 16521224

# Program GambarPita
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar pita sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: "Masukan tidak valid"

# KAMUS
# Variabel
#    N : int

def GambarPita(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar pita dengan lebar sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    Z = (N+1)//2
    li = [0 for i in range (Z)]
    for i in range(Z):
        if i == 0:
            li[i] = 1
        else:
            li[i] = li[i-1] + 2
            
    Y = Z
    li_reverse = [0 for i in range (Z)]
    for i in li:
        Y -= 1
        li_reverse[Y] = i

    i_reverse = 1
    for i in range(N):
        if (i+1) <= (Z):
            print((' ' * i) + ('*' * li_reverse[i]))
        else:
            print((' ' * (N-(i+1))) + ('*' * li[i_reverse]))
            i_reverse += 1

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
# KAMUS
# cek : bool
# ALGORITMA
    if (N > 0) and (N % 2 == 1):
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N)):  # lengkapi dengan pemanggilan fungsi IsValid
    GambarPita(N)    # lengkapi dengan pemanggilan prosedur GambarPita
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")