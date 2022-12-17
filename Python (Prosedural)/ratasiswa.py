# Program RataRataSiswa
# Spesifikasi : membaca data siswa dari suatu tempat kursus dari suatu file teks
# dan menuliskan nilai rata-rata setiap siswa ke layar. Nilai rata-rata ditampilkan
# terurut berdasarkan NoInduk siswa.
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
    i = 0
    sum = 0
    count = 0
    for j in range(jumlah):
        current_NoInduk = list_siswa[i][0]
        if list_siswa[j][0] == current_NoInduk:
            sum += list_siswa[j][2]
            count += 1
        else:
            print(current_NoInduk+'='+str("{:.2f}".format(sum/count)))
            i = j
            sum = list_siswa[j][2]
            count = 1

        if j == (jumlah-1):
            print(list_siswa[j][0]+'='+str("{:.2f}".format(sum/count)))    