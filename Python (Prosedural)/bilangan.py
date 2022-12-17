# BILANGAN
# Membuat program yang membaca sebuah integer positif N dan memvalidasi N sampai didapatkan
# nilai N yang benar, yaitu 0 < N <= 100. Setelah mendapatkan nilai N yang benar, program
# meminta masukan N buah bilangan integer. Selanjutnya, program menerima masukan sebuah integer,
# misalnya X, dan menghasilkan hasil sesuai ketentuan pada soal.

# KAMUS
# N, X, i = int
# cek, cek1 = bool
# li = list

# ALGORITMA
N = int(input())
cek = False
while cek == False:
    if 0 < N <= 100:
        cek = True
        li = [0 for i in range(N)]
        for i in range(N):
            li[i] = int(input())
        X = int(input())
        cek1 = False
        if X == 0:
            for i in range(N):
                if li[i] == 0:
                    cek1 = True
                    break
            if cek1 == False:
                print("Tidak ada 0")
            else:
                print(i+1)
        elif X == -1:
            for i in range(N):
                if li[i] < 0:
                    cek1 = True
                    break
            if cek1 == False:
                print("Tidak ada negatif")
            else:
                print(i+1, li[i])
        elif X == 1:
            for i in range(N):
                if li[i] > 0:
                    cek1 = True
                    break
            if cek1 == False:
                print("Tidak ada positif")
            else:
                print(i+1, li[i])
        else:
            print("Tidak diproses")
    else:
        print("Masukan salah. Ulangi!")
        N = int(input())