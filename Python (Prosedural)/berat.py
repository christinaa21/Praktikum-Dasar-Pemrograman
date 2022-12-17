# BERAT
# Membuat program yang membaca masukan berat tubuh mahasiswa (dalam bentuk angka) dalam suatu kelas,
# sampai pengguna mengetikkan -999 (-999 tidak termasuk nilai yang diproses). Nilai yang valid berada
# dalam range 30-200 (30 dan 200 termasuk). Jika ada data nilai yang salah, maka data tersebut diabaikan
# (tidak termasuk dalam pemrosesan). Lalu, program menuliskan jumlah keseluruhan mahasiswa, jumlah mahasiswa
# dengan berat <= 50, jumlah mahasiswa dengan berat >= 100, dan rata-rata berat mahasiswa (dalam bentuk pembulatan).
# Jika pengguna dari awal mengetikkan -999 atau tidak ada data yang valid, tuliskan pesan "Data kosong".

# KAMUS
# berat, jumlah_mhs, kurang50, lebih100, sum = int

# ALGORITMA
berat = int(input())
jumlah_mhs = 0
kurang50 = 0
lebih100 = 0
sum = 0
while (berat != -999):
    if 30 <= berat <= 200:
        jumlah_mhs += 1
        if berat <= 50:
            kurang50 += 1
        elif berat >= 100:
            lebih100 += 1 
        sum += berat
    berat = int(input())
if jumlah_mhs == 0:
    print("Data kosong")
else:
    print(jumlah_mhs)
    print(kurang50)
    print(lebih100)
    print(round(sum/jumlah_mhs))