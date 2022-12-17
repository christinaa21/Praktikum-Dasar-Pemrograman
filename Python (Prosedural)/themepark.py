# THEME PARK
# Membuat program yang membaca input 3 buah integer, misalnya t, b, dan k
# dengan t mewakili tinggi badan seseorang (dalam cm, bernilai > 0), b mewakili
# berat badan seseorang (dalam kg, bernilai > 0), dan k mewakili suatu kategori
# kendaraan atraksi (bernilai 0..4). Program menuliskan TRUE ke layar jika orang
# dengan tinggi t dan berat b, boleh menaiki kendaraan atraksi dengan kategori k
# sesuai dengan ketentuan di atas dan FALSE jika tidak. Jika tidak boleh menaiki
# kategori apa pun, berarti nilai k = 0.

# KAMUS
# t, b, k = int

# ALGORITMA
t = int(input())
b = int(input())
k = int(input())

if t > 100 and b <= 150:
    if k > 1:
        print("TRUE")
    else:
        print("FALSE")
elif t <= 100:
    if b < 30:
        if k == 1:
            print("TRUE")
        else:
            print("FALSE")
    elif 30 < b <= 150:
        if ((k == 1) or (k==2)):
            print("TRUE")
        else:
            print("FALSE")
    elif b > 150:
        if k == 2:
            print("TRUE")
        else:
            print("FALSE")
elif 100 < t <= 200 and b > 150:
    if ((k == 2) or (k==3)):
        print("TRUE")
    else:
        print("FALSE")
else:
    if k == 0:
        print("TRUE")
    else:
        print("FALSE")