# SEGITIGA
# Membuat program yang menghitung luas segitiga dengan rumus 0,5 * alas * tinggi (dan hasilnya dibulatkan
# ke integer terdekat) dari masukan berupa alas dan tinggi (dalam bentuk integer). Masukan harus divalidasi
# sehingga selalu > 0. Jika masukan <= 0, program akan mengeluarkan pesan error.

# KAMUS
# a, t, l = float

# ALGORITMA
semua = input()
first = ''
second = ''

i = 0
cek = False
while (not cek):
    if semua[i] != ' ':
        first += semua[i]
        i += 1
    else:
        second += semua[i+1:]
        cek = True

a = int(first)
t = int(second)
# a, t = input().split()
if ((int(a) <= 0) or (int(t) <= 0)):
    print("Alas dan tinggi harus > 0")
else:
    l = 0.5 * int(a) * int(t)
    print(round(l))