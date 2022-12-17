# KONVERSI SUHU
# Membuat program yang menerima masukan 1 buah nilai bertipe real, misalnya t, yang merupakan besaran suhu dalam derajat Celcius;
# dan 1 buah kode satuan suhu konversi bertipe karakter, misalnya k, yang diasumsikan bernilai 'R' (Reamur), 'F' (Fahrenheit),
# atau 'K' (Kelvin); lalu mengkonversi suhu dari satuan Celcius ke satuan suhu yang lain, yaitu Fahrenheit, Reamur, atau Kelvin.

# KAMUS
# t = float
# k = str

# ALGORITMA
t = float(input())
k = input()
if k == 'R':
    print('{:.2f}'.format((4/5) * t))
elif k == 'F':
    print('{:.2f}'.format((9/5) * t + 32))
elif k == 'K':
    print('{:.2f}'.format(273.15 + t))