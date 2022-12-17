# RESISTOR
# Membuat program yang menerima 3 (tiga) bilangan riil yang merepresentasikan nilai resistor
# R1, R2, dan R3, berupa bilangan rill > 0, dan menghitung nilai resistansi total, tergantung
# dihubungkan secara serial atau paralel (asumsikan tidak ada jenis hubungan lain). Hubungan
# antar ketiga resistor dinyatakan dengan sebuah character pilihan. Jika pilihan = ‘s’ atau ‘S’
# berarti hubungan serial; jika pilihan = ‘p’ atau ‘P’, berarti hubungan paralel.


# KAMUS
# R1, R2, R3 = float
# pilihan = str
# benar = bool

# ALGORITMA
R1 = float(input())
R2 = float(input())
R3 = float(input())
pilihan = str(input())

benar = False
while benar == False:
    if ((R1 > 0) and (R2 > 0) and (R3 > 0)) and ((pilihan == 's') or (pilihan == 'S') or (pilihan == 'p') or (pilihan == 'P')):
        benar = True
        if (pilihan == 's') or (pilihan == 'S'):
            print("%.2f" % (R1 + R2 + R3))
        else:
            print("%.2f" % ((R1*R2*R3)/((R1*R2) + (R2*R3) + (R3*R1))))
    else:
        print("Masukan salah")
        R1 = float(input())
        R2 = float(input())
        R3 = float(input())
        pilihan = str(input())