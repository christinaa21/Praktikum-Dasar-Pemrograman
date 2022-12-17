# Program SortSaham
# Spesifikasi: membaca data kepemilikan saham sebuah perusahaan dari suatu file teks dan
# mengurutkan data tersebut ke layar berdasarkan IdPemilik secara terurut membesar serta
# menuliskan kembali data tersebut dalam keadaan terurut ke layar.
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
    for baris in list_saham:
        print(baris[0]+','+baris[1]+','+str(baris[2]))