# NILAI
# Membuat program yang membaca masukan sejumlah nilai mahasiswa (dalam bentuk angka) untuk sebuah kelas mata kuliah,
# sampai pengguna mengetikkan -9999 (-9999 tidak termasuk nilai yang diproses). Nilai yang valid berada
# dalam range 0-100. Jika ada data nilai yang salah, maka data tersebut diabaikan (tidak termasuk dalam pemrosesan).
# Lalu, program menuliskan jumlah keseluruhan mahasiswa, jumlah mahasiswa yang lulus (nilai >= 40), jumlah mahasiswa
# yang tidak lulus (nilai < 40), dan rata-rata nilai (tuliskan dengan 2 angka di belakang koma), untuk data-data yang valid.
# Jika tidak ada data yang valid, tuliskan 0 (menunjukkan banyaknya mahasiswa).
# Jika pengguna dari awal mengetikkan -9999, tuliskan pesan "Data nilai kosong".

# KAMUS
# nilai, lulus, tidak_lulus, sum = int

# ALGORITMA
nilai = int(input())
lulus = 0
tidak_lulus = 0
sum = 0
if nilai == -9999:
    print("Data nilai kosong")
else:
    while (nilai != -9999):
        if 0 <= nilai <= 100:
            sum += nilai
            if nilai >= 40:
                lulus += 1
            elif nilai < 40:
                tidak_lulus += 1 
        nilai = int(input())
    if (lulus + tidak_lulus) == 0:
        print(lulus + tidak_lulus)
    else:
        print(lulus + tidak_lulus)
        print(lulus)
        print(tidak_lulus)
        print("%.2f" % (sum/(lulus + tidak_lulus)))