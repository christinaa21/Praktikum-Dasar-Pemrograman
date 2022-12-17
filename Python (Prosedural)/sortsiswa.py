# Program SortSiswa
# Spesifikasi : membaca data siswa dari suatu tempat kursus dari suatu file teks dan
# mengurutkan data tersebut ke layar berdasarkan NoInduk secara terurut membesar serta
# menuliskan kembali data tersebut dalam keadaan terurut ke layar.
import tulisdata

# KAMUS
# namafile: string
# mark = 99999999 # constant mark
# type dataSiswa  : <NoInduk: string,
#                    KodeKursus : string,
#                    Nilai : integer>

# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)

f = open(namafile)
baris = f.readlines()
f.close()

i = 0
jumlah = 0
list_siswa = []

while baris[i] != '99999999':
    NoInduk = baris[i].replace('\n', '')
    KodeKursus = baris[i+1].replace('\n', '')
    Nilai = int(baris[i+2])
    list_siswa += [(NoInduk, KodeKursus, Nilai)]
    i += 3
    jumlah += 1

# Insertion Sort Method
for Pass in range(1, jumlah):
    Temp = list_siswa[Pass]
    i = Pass-1
    while (Temp[0] < list_siswa[i][0]) and (i > 1):
        list_siswa[i+1] = list_siswa[i]
        i = i-1
    if (Temp[0] >= list_siswa[i][0]):
        list_siswa[i+1] = Temp
    else:
        list_siswa[i+1] = list_siswa[i]
        list_siswa[i] = Temp

if jumlah == 0:
    print("File kosong")
else:
    for baris in list_siswa:
        print(baris[0]+','+baris[1]+','+str(baris[2]))