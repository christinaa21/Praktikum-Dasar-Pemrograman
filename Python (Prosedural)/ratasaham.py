# Program RataRataSaham
# Spesifikasi: membaca data kepemilikan saham sebuah perusahaan dari suatu file teks dan
# menuliskan nilai rata-rata nilai saham yang dimiliki oleh setiap pemilik. Nilai rata-rata
# saham untuk setiap pemilik ditampilkan terurut berdasarkan IdPemilik.
import tulisdata1

# KAMUS
#namafile: string
# mark = 99999999 # constant mark
#type dataSaham  : <IdPemilik : string, { Kode Pemilik Saham }
#                   IdPT : string,      { Kode Perusahaan }
#                   Nilai : integer>    { Nilai saham, dalam juta rupiah }

# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata1.TulisDataSaham(namafile)

f = open(namafile)
baris = f.readlines()
f.close()

i = 0
jumlah = 0
list_saham = []

while baris[i] != '99999999':
    IdPemilik = baris[i].replace('\n', '')
    IdPT = baris[i+1].replace('\n', '')
    Nilai = int(baris[i+2])
    list_saham += [(IdPemilik, IdPT, Nilai)]
    i += 3
    jumlah += 1

# Insertion Sort Method
for Pass in range(1, jumlah):
    Temp = list_saham[Pass]
    i = Pass-1
    while (Temp[0] < list_saham[i][0]) and (i > 1):
        list_saham[i+1] = list_saham[i]
        i = i-1
    if (Temp[0] >= list_saham[i][0]):
        list_saham[i+1] = Temp
    else:
        list_saham[i+1] = list_saham[i]
        list_saham[i] = Temp

if jumlah == 0:
    print("File kosong")
else:
    i = 0
    sum = 0
    count = 0
    for j in range(jumlah):
        current_IdPemilik = list_saham[i][0]
        if list_saham[j][0] == current_IdPemilik:
            sum += list_saham[j][2]
            count += 1
        else:
            print(current_IdPemilik+'='+str("{:.2f}".format(sum/count)))
            i = j
            sum = list_saham[j][2]
            count = 1

        if j == (jumlah-1):
            print(list_saham[j][0]+'='+str("{:.2f}".format(sum/count)))