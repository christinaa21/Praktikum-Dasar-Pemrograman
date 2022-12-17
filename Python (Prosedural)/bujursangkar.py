# BUJUR SANGKAR
# Membuat program yang menghitung luas bujur sangkar (persegi) dengan rumus sisi * sisi, dari masukan
# berupa sisi (dalam bentuk integer). Input sisi harus divalidasi sehingga selalu > 0. Jika sisi yang
# dimasukkan <= 0, program akan mengeluarkan pesan error.

# KAMUS
# sisi = integer

# ALGORITMA
sisi = int(input())
if sisi <= 0:
    print("Sisi harus > 0")
else:
    print(sisi * sisi)