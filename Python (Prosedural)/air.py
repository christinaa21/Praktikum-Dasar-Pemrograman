# AIR
# Membuat program yang membaca sebuah nilai T, suatu bilangan integer yang menyatakan
# temperatur air dalam derajat celcius untuk kondisi tekanan 1 atm.  Program menuliskan
# apakah kondisi air tersebut tergantung kepada temperaturnya dengan menyesuaikan 5 kondisi
# yang tertera pada soal dan mungkin sesuai kaidah fisika.

# KAMUS
# T = int

# ALGORITMA
T = int(input())
if T < 0:
    print("PADAT")
elif T == 0:
    print("ANTARA PADAT-CAIR")
elif 0 < T < 100:
    print("CAIR")
elif T == 100:
    print("ANTARA CAIR-GAS")
else:
    print("GAS")