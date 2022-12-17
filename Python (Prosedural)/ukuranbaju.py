# UKURAN BAJU
# Membuat program yang membaca masukan 2 buah integer positif, misalnya t (tinggi badan dalam cm)
# dan b (berat badan dalam kg) dan menuliskan kode ukuran baju (1=M, 2=L, 3=XL, 4=tidak mendapat kaos).

# KAMUS
# t, b = int

# ALGORITMA
t = int(input())
b = int(input())

if (t and b) >= 0:
    if t <= 150:
        print("1")
    elif 150 < t <= 170:
        if b <= 80:
            print("2")
        else:
            print("3")
    elif t > 170 and 60 < b <= 80:
        print("3")
    else:
        print("4")
else:
    print("4")