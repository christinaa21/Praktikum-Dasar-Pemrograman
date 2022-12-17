# cARI CHARACTER
# Membuat program yang membaca sebuah integer positif N, yang harus divalidasi sampai didapatkan
# nilai N yang benar, yaitu 0 < N <= 100. Jika masukan N salah, tuliskan pesan "Masukan salah. Ulangi!".
# Setelah didapatkan nilai N yang benar, program meminta masukan N buah character. Lalu, program menerima
# masukan sebuah character, misalnya CC, dan menghasilkan hasil sesuai yang tertera pada ketentuan soal.

# KAMUS
# N = int
# CC = str

# ALGORITMA
N = int(input())
while (N <= 0) or (N > 100):
    print("Masukan salah. Ulangi!")
    N = int(input())

list_N = [0 for i in range(N)]
for i in range(N):
    list_N[i] = input()[0]

list_ascii = [0 for i in range(N)]
for i in range(N):
    list_ascii[i] = ord(list_N[i])

CC = input()
ada = False
if (CC == 'S') or (CC == 's'):
    for i in range(N):
        if 97 <= list_ascii[i] <= 122:
            print(i+1, chr(list_ascii[i]))
            ada = True
            break
    if ada == False:
        print("Tidak ada huruf kecil")
elif (CC == 'L') or (CC == 'l'):
    for i in range(N):
        if 65 <= list_ascii[i] <= 90:
            print(i+1, chr(list_ascii[i]))
            ada = True
            break
    if ada == False:
        print("Tidak ada huruf besar")
elif (CC == 'X') or (CC == 'x'):
    for i in range(N):
        if not(97 <= list_ascii[i] <= 122) and not(65 <= list_ascii[i] <= 90):
            print(i+1, chr(list_ascii[i]))
            ada = True
            break
    if ada == False:
        print("Semua huruf")
else:
    print("Tidak diproses")