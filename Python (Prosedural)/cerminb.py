# Nama: Christina Wijaya
# NIM: 16521224

# Program GambarBTercermin
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar B tercermin sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarBTercermin(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar B tercermin dengan lebar sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    Z = (N+1)//2
    for i in range(0, Z+1):
        if i == 0:
            print('*' * (N - (2*i)))
        else:
            if (N - (2*i)) > 0:
                print((' ' * (2*i)) + ('*' * (N - (2*i))))
    for i in range(Z-1, 0, -1):
        for j in range(0, Z+1):
            if i != 0:
                if i == 1:
                    print('*' * N)
                    break
                else:
                    if j % 2 == 0:
                        print((' ' * i) + ('*' * (N - i)))
                    else:
                        print((' ' * (2*(i-1))) + ('*' * (N - (2*i))))

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    if (N > 0) and (N % 2 == 1):
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N)):  # lengkapi dengan pemanggilan fungsi IsValid
    GambarBTercermin(N)    # lengkapi dengan pemanggilan prosedur GambarBTercermin
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")