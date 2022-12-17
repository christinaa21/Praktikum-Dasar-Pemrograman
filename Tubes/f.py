import os
import argparse
from datetime import date

# Cara me-run program: python ProsedurFungsi.py -f FolderFile

# ------------------------------------------------------------- F02 -------------------------------------------------------------- #
def convert(string):
    arr = []
    arr[:0] = string
    return arr

def register():
    # Mendaftarkan pengguna baru dengan memasukkan nama, username, dan password.
    # I.S. Data user terdefinisi
    # F.S. Data user baru berhasil ditambahkan dalam variabel user
    
    global user

    name = input("Masukan nama: ")
    uname = input("Masukan username: ")
    pwd = input("Masukan password: ")
    id = length(user)
    count = length(user)
    uname_char = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P',
                  'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    acc_char = 0

    for i in range(1, (length(user))):
        if ((user[i][1]) == uname):
            count -= 1

    arr_uname = convert(uname)

    if (count == ((length(user))-1)):
        print("Sayang sekali, username", uname,
              "sudah terdaftar :(. Silakan coba masukan username lain.")
    else:
        for i in range(length(arr_uname)):
            for j in range(length(uname_char)):
                if uname[i] == uname_char[j]:
                    acc_char += 1
        if acc_char != length(arr_uname):
            print("Username mengandung karakter yang tidak diperbolehkan. Mohon hanya gunakan abjad (A-Z atau a-z), underscore (_), tanda strip (-), atau angka (0-9) saja. Jangan gunakan spasi.")
        else:
            user += [[id, uname, name, pwd, "User", 0]]
            print("Selamat! User", uname,
                  "telah berhasil melakukan register ke dalam BNMO.")

# ------------------------------------------------------------- F03 -------------------------------------------------------------- # 
def login():
    global uname
    global id_user
    global userkah
    global sudah_login

    uname = input("Masukkan username: ")
    pwd = input("Masukkan password: ")
    
    check = False
    for i in range(length(user)):
        if (str(user[i][1]) == uname) and (str(user[i][3]) == pwd):
            check = True
            id_user = user[i][0]
            if user[i][4] == 'User':
                userkah = True
            else:
                userkah = False
            sudah_login = True
            sambutan = "Halo " + user[i][2] + '! Selamat datang di "Binomo".'
            border(sambutan, '#')
            break
    if check == False:
        print("Password atau username salah atau tidak ditemukan.")
    return sudah_login
            
# ------------------------------------------------------------- F04 -------------------------------------------------------------- #
def tambah_game():
    # Menambah data game baru pada variabel data_game
    # I.S. data game terdefinisi
    # F.S. data_game bertambah data game baru beserta informasinya  

    global data_game
    cek=False   
    while cek==False :
        nama_game=input("Masukkan nama game: ")
        kategori=input("Masukkan kategori: ")
        tahun_rilis=(input("Masukkan tahun rilis: "))
        harga=input("Masukkan harga: ")
        stok_game=(input("Masukkan stok awal: "))
        if nama_game=="" or kategori=="" or tahun_rilis=="" or harga=="" or stok_game=="":
            cek=False
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else:
            cek=True
            
    if cek==True:
        print("Selamat! Berhasil menambahkan game BNMO",nama_game)
        # menambah list pada matriks game
        baris=length(data_game)
        # asumsi
        if baris>0 and baris<10:
            nol='00'
        elif baris>=10 and baris<100:
            nol='0'
        else :
            nol=''
        id_game='G'+nol+str(baris)
        data_game+=[[id_game,nama_game,kategori,tahun_rilis,harga,stok_game]]
    return data_game

# ------------------------------------------------------------- F05 -------------------------------------------------------------- #
def ubah_game ():
    # Mengubah game pada toko game melalui pengisian informasi game yang akan diubah.
    # I.S. data game terdefinisi
    # F.S. data game berubah menjadi data-data baru yang sudah dimasukkan user

    # KAMUS LOKAL
    # id_game,nama_game,kategori,tahun_rilis_harga : string 

    # ALGORITMA
    id_game=input("Masukkan ID game: ")
    nama_game=input("Masukkan nama game: ")
    kategori=input("Masukkan kategori: ")
    tahun_rilis=input("Masukkan tahun rilis: ")
    harga=input("Masukkan harga: ")

    for i in range (length(data_game)):
        if data_game[i][0]==id_game:
            X=i
            data_game_valid=True
    if data_game_valid:
        if nama_game !='':
            data_game[X][1]=nama_game
        if kategori !='':
            data_game[X][2]=kategori
        if tahun_rilis !='':
            data_game[X][3]=int(tahun_rilis)
        if harga !='':
            data_game[X][4]=int(harga)


    return data_game #data_game di return 

# ------------------------------------------------------------- F06  -------------------------------------------------------------- #
def ubah_stok():
    # Mengubah jumlah stok_game pada data dalam variabel data_game 
    # I.S. Data tedefinisi
    # F.S. Stok dari data_game berubah (bertambah atau berkurang atau stok kurang)

    cek1 = False
    cek2 = False
    global kepemilikan
    global riwayat
    while cek1==False:
        try:
            id_game=input("Masukkan ID Game: ")
            
            # for i in range(length(data_game)):
            #     if user[i][0]==id_user:
            #         id=i 
            
            # mengecek id_game
            for i in range(length(data_game)):
                if data_game[i][0]==id_game:
                    baris = i
                    cek1=True
                
            if cek1==False:
                print("Tidak ada game dengan ID tersebut!")
        except ValueError:
            print()
    # mengecek stok game
    for i in range(length(data_game)):
        if data_game[i][0]==id_game and data_game[i][5] > 0:
            cek2=True

    if cek2==False:
            print("Stok Game tersebut sudah habis!")
    # mengubah stok game
    else:
        jumlah=int(input("Masukkan jumlah: "))
        if jumlah > 0:
            penjumlahan="ditambahkan"
        else:
            penjumlahan="dikurangi"
        data_game[baris][5]+=jumlah

    # print(cek1,cek2)
    if cek1==True and cek2==True :
        if data_game[baris][5] >=0:
            print("Stok game "+ str(data_game[baris][1]) +" berhasil "+str(penjumlahan)+". Stok sekarang: "+str(data_game[baris][5]))          
        else:
            print("Stok game "+ str(data_game[baris][1]) +" gagal "+str(penjumlahan)+" karena stok kurang. Stok sekarang: 1 (<10)")

# ------------------------------------------------------------- F07  -------------------------------------------------------------- #
def list_game_toko(data_game):
    data_game = filter(data_game, 0)
    sorting = input("Skema sorting : ")
    if sorting == 'tahun-' or sorting == 'tahun+' or sorting == 'harga-' or sorting == 'harga+':
        if sorting == 'tahun-':
            for i in range(length(data_game)):
                IMax = i
                for j in range(i+1, length(data_game)):
                    if (data_game[IMax][3] < data_game[j][3]):
                        IMax = j
                Temp = data_game[IMax]
                data_game[IMax] = data_game[i]
                data_game[i] = Temp
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
        elif sorting == 'tahun+':
            for i in range(length(data_game)):
                IMax = i
                for j in range(i+1, length(data_game)):
                    if (data_game[IMax][3] > data_game[j][3]):
                        IMax = j
                Temp = data_game[IMax]
                data_game[IMax] = data_game[i]
                data_game[i] = Temp
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
        elif sorting == 'harga+':
            for i in range(length(data_game)):
                IMax = i
                for j in range(i+1, length(data_game)):
                    if (data_game[IMax][4] > data_game[j][4]):
                        IMax = j
                Temp = data_game[IMax]
                data_game[IMax] = data_game[i]
                data_game[i] = Temp
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
        elif sorting == 'harga-':
            for i in range(length(data_game)):
                IMax = i
                for j in range(i+1, length(data_game)):
                    if (data_game[IMax][4] < data_game[j][4]):
                        IMax = j
                Temp = data_game[IMax]
                data_game[IMax] = data_game[i]
                data_game[i] = Temp
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
        elif sorting == '':
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
    else:
        print("Skema sorting tidak valid!")

# ------------------------------------------------------------- F08 -------------------------------------------------------------- #
def buy_game():
    # Membeli game dari toko, menambah riwayat dari pembelian game, menambah kepemilikan game pengguna
    # I.S. riwayat, data_game, kepemilikan terdefinisi
    # F.S. game tertambah dalam data kepemilikan, riwayat, dan stok game berkurang

    cek1 = False
    cek2 = True
    cek3 = False
    cek4 = False
    global kepemilikan
    global riwayat
    # print(data_game[0][0])
    try:
        id_game=input("Masukkan ID Game: ")
        for i in range(length(user)): #length(data_game)
            # print(i)
            if user[i][0]==id_user:
                id=i 

        # mengecek id_game
        for i in range(length(data_game)):
            if data_game[i][0]==id_game:
                baris = i
                cek1=True
        if cek1==False:
            print("ID Game yang Anda masukan salah\n")
        else:
            # mengecek kepemilikan game 
            for i in range(length(kepemilikan)):
                if kepemilikan[i][1]==id_user and kepemilikan[i][0]==id_game: #Kalau dia punya gamenya
                        cek2 = False
            if cek2==False:
                print("Anda sudah memiliki Game tersebut!")
            else :
                # mengecek saldo
                if user[id][5] >= data_game[baris][4]:
                    cek3=True

                if cek3==False:
                    print("Saldo Anda tidak cukup untuk membeli Game tersebut!")
                else:    
                    # mengecek stok game
                    for i in range(length(data_game)):
                        if data_game[i][0]==id_game and data_game[i][5] > 0:
                            cek4=True
                            # ketemu3=True
                    if cek4==False:
                            print("Stok Game tersebut sudah habis!")
    except ValueError:
        print()
    # print(cek1,cek2,cek3,cek4)
    if cek1==True and cek2==True and cek3==True and cek4==True :          
        # mengubah stok game 
        data_game[baris][5]-=1

        # mengurangi saldo user
        user[id][5]-= data_game[baris][4]

        # menambah kepemilikan
        kepemilikan += [[id_game,id_user]]  
        # kepemilikan += tambah(kepemilikan, [id_game,id_user])

        # menambah riwayat
        riwayat += [[id_game,data_game[baris][1],data_game[baris][4],id_user,date.today().year]]
        
        print('''Game "'''+str(data_game[baris][1])+'''" berhasil dibeli!''')

# ------------------------------------------------------------- F09  -------------------------------------------------------------- #
def list_game():
    # Menampilkan daftar game yang dimiliki pengguna 
    # I.S. data kepemilikan, data_game terdefinisi 
    # F.S. list game ditampilkan di layar

    count = 0
    arr = [0 for i in range(100)]
    for i in range(1, length(kepemilikan)):
        if kepemilikan[i][1] == uname:
            arr[i-1] = kepemilikan[i][0]

    print("Daftar game milikmu:")
    # print(kepemilikan)
    for i in range(0, length(arr)):
        for j in range(1, (length(data_game))):
            if arr[i] == data_game[j][0]:
                count += 1
                print(count, end="")
                print(".", end=" ")
                for l in range(0, 6):
                    print(data_game[j][l], end=" ")
                    if l != 5:
                        print("|", end=" ")
                    else:
                        print("|")
    if count == 0:
        print("-")
        print("Ups, kamu belum memiliki game. Yuk beli game terlebih dahulu dengan menuliskan command 'buy game'!")

# ------------------------------------------------------------- F10 -------------------------------------------------------------- #
def search_my_game():
    # Mencari game dengan ID
    # I.S.
    # F.S.

    id_game = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print("\nDaftar game pada inventory yang memenuhi kriteria:")

    punya = 0
    punya1 = 0
    punya2 = 0
    punya3 = 0
    for i in range(length(riwayat)):
        if riwayat[i][3] == id_user:
            punya += 1
            if id_game == "" and tahun_rilis == "":
                nomor = 1
                for j in range(length(data_game)):
                    if data_game[j][0] == riwayat[i][0]:
                        print(str(nomor) + ". " + data_game[j][0] + " | " + data_game[j][1] + " | " + str(data_game[j][4]) + " | " + data_game[j][2] + " | " + str(data_game[j][3]))
                    nomor += 1
            elif tahun_rilis == "":
                nomor = 1
                for j in range(length(data_game)):
                    if (data_game[j][0] == riwayat[i][0]) and (data_game[j][0] == id_game):
                        punya1 += 1
                        print(str(nomor) + ". " + data_game[j][0] + " | " + data_game[j][1] + " | " + str(data_game[j][4]) + " | " + data_game[j][2] + " | " + str(data_game[j][3]))
                        nomor += 1
            else:
                try:
                    tahun_rilis = int(tahun_rilis)
                    if tahun_rilis < 0:
                        print("Tahun rilis game tidak boleh negatif")
                        break
                    else:
                        if id_game == "":
                            nomor = 1
                            for j in range(length(data_game)):
                                if (data_game[j][0] == riwayat[i][0]) and (data_game[j][3] == tahun_rilis):
                                    punya2 += 1
                                    print(str(nomor) + ". " + data_game[j][0] + " | " + data_game[j][1] + " | " + str(data_game[j][4]) + " | " + data_game[j][2] + " | " + str(data_game[j][3]))
                                    nomor += 1
                        else:
                            nomor = 1
                            for j in range(length(data_game)):
                                if (data_game[j][0] == riwayat[i][0]) and (data_game[j][0] == id_game) and (data_game[j][3] == tahun_rilis):
                                    punya3 += 1
                                    print(str(nomor) + ". " + data_game[j][0] + " | " + data_game[j][1] + " | " + str(data_game[j][4]) + " | " + data_game[j][2] + " | " + str(data_game[j][3]))
                                    nomor += 1
                except ValueError:
                    print("Tahun rilis game harus merupakan bilangan bulat")
                    break
    if punya == 0:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        if tahun_rilis == "" and id_game != "" and punya1 == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        elif tahun_rilis != "" and id_game == "" and punya2 == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        elif id_game != "" and tahun_rilis != "" and punya3 == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

# ------------------------------------------------------------- F11 -------------------------------------------------------------- #
def search_game_at_store(data_game):
    # Mencari game  
    # I.S. 
    # F.S. 

    data_game = filter(data_game, 0)
    check = True

    id_game = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print("\nDaftar game pada toko yang memenuhi kriteria:")

    if id_game:
        for i in range(length(data_game)-1, -1, -1):
            if data_game[i][0] != id_game:
                data_game = filter(data_game, i)
    if nama_game:
        for i in range(length(data_game)-1, -1, -1):
            if data_game[i][1] != nama_game:
                data_game = filter(data_game, i)
    if kategori:
        for i in range(length(data_game)-1, -1, -1):
            if data_game[i][2] != kategori:
                data_game = filter(data_game, i)
    if tahun_rilis:
        try:
            tahun_rilis = int(tahun_rilis)
            if tahun_rilis < 0:
                print("Tahun rilis game tidak boleh negatif")
                check = False
            else:
                for i in range(length(data_game)-1, -1, -1):
                    if data_game[i][3] != tahun_rilis:
                        data_game = filter(data_game, i)
        except ValueError:
            print("Tahun rilis game harus merupakan bilangan bulat")
            check = False
    if harga:
        try:
            harga = int(harga)
            if harga < 0:
                print("Harga game tidak boleh negatif")
                check = False
            else:
                for i in range(length(data_game)-1, -1, -1):
                    if data_game[i][4] != harga:
                        data_game = filter(data_game, i)
        except ValueError:
            print("Harga game harus merupakan bilangan bulat")
            check = False
    if check == True:
        if data_game:
            for i in range(length(data_game)):
                print(str(i + 1) + ". " + data_game[i][0] + " | " + data_game[i][1] + " | " + str(data_game[i][4]) + " | " + data_game[i][2] + " | " + str(data_game[i][3]) + " | " + str(data_game[i][5]))
        else:
            print("Tidak ada game pada toko yang memenuhi kriteria")

# ------------------------------------------------------------- F12 -------------------------------------------------------------- #
def topup():
    # PROGRAM penambahan atau pengurangan saldo yang dapat diakses admin. Apabila saldo berujung minus, sistem akan menolak masukan.
    # I.S. Saldo awal terdefinisi
    # F.S. Saldo berubah dari keadaan awal (dapat bertambah atau berkurang)

    global user
    
    username = input("Masukan username: ")
    saldo = int(input("Masukan saldo: "))
    count = length(user)
    index = 0
    
    # asumsi urutan kolom pada data csv: name;uname;pwd;saldo
    # pengulangan untuk menemukan username yang cocok dengan masukan user
    for i in range (1, length(user)):
        # percabangan untuk menemukan username yang cocok
        if ((user[i][1]) == username):
            count -=1
            index = i
    # percabangan jika sistem telah melakukan pengecekan pada file csv
    if (count == (length(user) - 1)):
        # percabangan jika ditemukan username yang cocok pada file csv
        if (saldo*(-1)) > int(user[index][5]) and saldo < 0:
            print("Masukan tidak valid.")
        else: #saldo <= int(user[index][5])
            saldo_new = int(user[index][5]) + saldo
            user[index][5] = saldo_new
            # percabangan jika saldo yang dimasukkan pengguna berupa pengurangan atau penambahan
            if saldo < 0:
                print("Top up berhasil. Saldo", user[index][2], "berkurang menjadi", saldo_new)
            else: # saldo >- 0 (bilangan positif)
                print("Top up berhasil. Saldo", user[index][2], "bertambah menjadi", saldo_new)
    else:
        print("Username", username, "tidak ditemukan.") 
     
# ------------------------------------------------------------- F13  -------------------------------------------------------------- #
def history(riwayat):
    riwayat = filter(riwayat, 0)
    for i in range(len(riwayat)-1, -1, -1):
        if riwayat[i][3] != id_user:
            riwayat = filter(riwayat, i)
    if riwayat:
        print("Daftar game:")
        for i in range(length(riwayat)):
            print(str(i + 1) + ". " + riwayat[i][0] + " | " + riwayat[i][1] + " | " + str(riwayat[i][2]) + " | " + str(riwayat[i][4]))
    else:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")

# ------------------------------------------------------------- F14  -------------------------------------------------------------- #
def help():  
    # Program menunjukkan serangkaian perintah menu yang dapat diakses dalam program
    # I.S. Program berjalan
    # F.S. Keluaran serangkaian menu yang bisa dipilih
    print('============ HELP ============')
    print("""1. register - Untuk melakukan registrasi user baru (Akses: Admin)
2. login - Untuk melakukan login ke dalam sistem (Akses: Admin dan User)
3. tambah_game - Untuk menambah game yang dijual pada toko (Akses: Admin)
4. ubah_game - Untuk mengubah informasi pada game yang akan ditampilkan pada toko (Akses: Admin)
5. ubah_stok - Untuk mengubah dan memvalidasi stok game pada toko (Akses: Admin)
6. list_game_toko - Untuk melihat sorted list game yang dijual pada toko (Akses: Admin dan User)
7. buy_game - Untuk membeli game dari toko (Akses: User)
8. list_game - Untuk melihat daftar game yang dimiliki user (Akses: User)
9. search_my_game - Untuk mencari semua game sesuai dengan 2 kriteria pencarian (Akses: User)
10. search_game_at_store - Untuk mencari game sesuai stok Toko dengan 5 kriteria pencarian
11. topup - Untuk menambahkan saldo pada user (Akses: Admin)
12. riwayat - Untuk melihat list riwayat pembelian game yg sudah dibeli (Akses: User)
13. help - Untuk menampilkna bantuan terkait serangkaian perintah menu yang dapat diakses dalam program (Akses: Admin dan User)
14. save - untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan (Akses: Admin dan User)
15. exit - Untuk keluar dari program. (Akses: Admin dan User)
""")

# ------------------------------------------------------------- F15 -------------------------------------------------------------- #
def load_data(file):
    # menerima input file csv dan mengoutputkan data kembali dalam bentuk matriks sesuai data csv
    # I.S. file terdefinisi
    # F.S. output matriks data sesuai file
    
    # KAMUS LOKAL
    # f : SEQFILE OF
    #       (*) raw_lines : array of string
    #       (1) mark : None 
    # arr : array of string
    # lines : array of string
    # data : string
    # arrALL : array of array of string
    
    # ALGORITMA
    f = open(file,"r")
    raw_lines = f.readlines()
    f.close()
    lines = []
    for i in range(length(raw_lines)):
        if i < length(raw_lines):
            lines += [strip_enter(raw_lines[i])]
    arrAll = []
    for line in lines:
        data =""
        arr = []
        for i in range(length(line)):
            if line[i] == ';':
                # jika bertemu ';' yang terdapat pada csv maka data akan ditambahkan ke arr
                arr += [data]
                data = ""
            elif (i == length(line) - 1):
                # menambahkan data yang paling belakang untuk ditambahkan ke arr
                arr += [data + line[i]]
            else:
                data += line[i]
        arrAll += [arr]
    return arrAll

def tryChange(data):
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika memungkinkan
    # I.S. data terdefinisi
    # F.S. output data elemen yang dapat diubah, yang sebelumnya array of string menjadi boolean atau integer
    
    # KAMUS LOKAL
    # i, j : integer
    
    # ALGORITMA
    for i in range(length(data)):
        for j in range(length(data[i])):
            try:
                # Mengubah data pada matriks menjadi integer jika memungkinkan
                data[i][j] = int(data[i][j])
            except:
                ValueError
            # Mengubah data pada matriks menjadi boolean jika memungkinkan
            if data[i][j] == "True":
                data[i][j] = True
            elif data[i][j] == "False":
                data[i][j] = False
    return data

def load(folder):
    # Membaca semua file csv dengan memanggil prosedur load_data dan tryChange
    # I.S. semua file csv sudah tersedia pada folder yang diinput
    # F.S. semua data pada file csv sudah diubah dalam bentuk matriks dengan tipe data yang sudah disesuaikan.

    # KAMUS LOKAL
    # user : array of data_user
    # game : array of data_game
    # riwayat : array of data_riwayat
    # kepemilikan : array of data_kepemilikan

    # Variable global
    global user
    global data_game
    global riwayat
    global kepemilikan
    # Function / Procedure
    # load_data(file : csv) -> array of array of string
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file

    # tryChange(data : array of array of string) -> any of data_user or data_gadget or data_consumable or data_gadget_return_history or 
    #                                               data_gadget_borrow_histroy or data_consumable_history or data_inventory_user
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah

    # ALGORITMA
    os.chdir('./' + str(folder))

    user = tryChange(load_data("user.csv"))
    data_game = tryChange(load_data("game.csv"))
    riwayat = tryChange(load_data("riwayat.csv"))
    kepemilikan = tryChange(load_data("kepemilikan.csv"))

    os.chdir('../')

def loading():
    # Mendapatkan directory folder csv dengan menggunakan argparse
    # I.S. Directory folder csv belum ada
    # F.S. Directory folder csv sudah ada, namun jika ternyata tidak ditemukan, akan dihasilkan None
    
    # KAMUS LOKAL
    # parser : ArgumentParser
    # directory, parent, path, csv : string
    # list_csv : array of string
    
    # ALGORITMA
    parser = argparse.ArgumentParser()
    
    # Menangani kasus error
    parser.add_argument("-f","--folder", type=str, help="Input nama folder csv (required)")  
    if parser.parse_args().folder is None:
        parser.error("""
\033[91m Tidak ada folder yang diinput. Silahkan input nama folder! \033[0m
\033[93m Format input : python main.py -f nama-folder-csv \033[0m""")
        return None
    
    # Berpindah directory ke folder csv
    directory = parser.parse_args().folder
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    
    # Validasi folder ada
    if not os.path.exists(path):
        print("Nama folder yang diinputkan tidak ada")
    else:
        os.chdir('./' + directory)
        list_csv = ["user.csv","game.csv","riwayat.csv","kepemilikan.csv"]
        for csv in list_csv:
            # Validasi file ada
            if not (os.path.exists(csv)):
                print(csv + " tidak ditemukan")
                return None
        # Berpindah directory ke parent
        os.chdir('../')
        return directory

# ------------------------------------------------------------- F16 -------------------------------------------------------------- #
def save_data(file,data):
    # Menulis data ke dalam csv
    # I.S. data terdefinisi
    # F.S. memperbarui file yang telah ada dan membuat file csv baru jika belum
    
    # KAMUS LOKAL
    # data : string
    # f : SEQFILES OF
    #       (*) array of string
    #       (1) mark : None
    
    # ALGORITMA
    data = convert_datas_to_string(data)
    f = open(file, "w") 
    f.write(data)
    f.close()

def convert_datas_to_string(data):
    # Mengubah data kembali menjadi string sesuai format agar dapat di-write ke dalam file csv
    # I.S. data terdefinisi
    # F.S. Dikembalikan string sesuai format
    
    # KAMUS LOKAL
    # data_string : string
    # arr_data : any of user or data_game or riwayat or kepemilikan
    # arr_data_all_string : array of string
    
    # ALGORITMA
    data_string = ""
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        data_string += ";".join(arr_data_all_string)
        data_string += "\n"
    return data_string

def save():
    # Menyimpan data ke dalam file di folder yang diinputkan
    # I.S. user, data_game, riwayat, kepemilikan terdefinisi
    # F.S. file user, data_game, riwayat, kepemilikan tersimpan

    # KAMUS LOKAL
    # parent, directory, path : string

    # Function / Procedure
    # save_data (file : csv, data : any of data_user or data_gadget or data_consumable or data_gadget_return_history or 
    #                               data_gadget_borrow_histroy or data_consumable_history or data_inventory_user)
    # Menulis data ke dalam file csv
    # I.S. data terdefinisi
    # F.S. memperbarui file yang telah ada dan membuat file csv baru jika belum

    # ALGORITMA
    parent = os.getcwd()

    # Validasi directory
    checkDir = False
    while not checkDir:
        checkDir = True
        directory = input("Masukkan nama folder penyimpanan: ")
        for i in range(length(directory)):
            if directory[i] in ('/\:*?"><|'):
                checkDir = False
                print('nama folder anda mengandung /\:*?"><|')
                print()

    path = os.path.join(parent, directory)
    
    try:
        # Membuat folder baru jika belum ada menggunakan os
        os.mkdir(path)
    except:
        FileExistsError

    # Berpindah directory ke dalam folder csv
    os.chdir('./' + directory)
    print()
    print("Saving...")
    # time.sleep(3)

    # Menyimpan file csv
    save_data("user.csv",user)
    save_data("game.csv",data_game)
    save_data("riwayat.csv",riwayat)
    save_data("kepemilikan.csv",kepemilikan)

    print("Data telah disimpan pada folder " + str(directory)) # mau di bold directory nya
    # Berpindah directory ke folder parent dengan os
    os.chdir('../')

# ------------------------------------------------------------- F17 -------------------------------------------------------------- #
def exit():
    #
    #
    #
    
    global end
    global sudah_login
    # while sudah_login==True:
    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    check = False
    while check == False:
        if simpan == 'Y' or simpan == 'y' :
            save()
            check = True           
            end = True
        elif  simpan == 'n' or simpan == 'N':
            check=True
            end = True
        else:
            simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        # end = True
    return end
# ------------------------------------------------------- Fungsi Tambahan -------------------------------------------------------- #
def length(list):
    count = 0
    for items in list:
        count += 1
    return count

def tambah(list, items):
    count = length(list)
    updated_list = ["" for i in range (count+1)]
    for i in range (count):
        updated_list[i] = list[i]
    updated_list[count] = items
    return updated_list

def split (string, delimeters= ';'):
    hasil = []
    char = ''
    for i in string:
        if i not in delimeters:
            char += i
        elif char:
            hasil = tambah(hasil, char)
            char = ''
    if char:
        hasil = tambah(hasil, char)
    return hasil

def filter(arrAll, baris):
    arrNew = []
    for i in range(baris):
        arrNew += [arrAll[i]]
    for i in range(baris+1, length(arrAll)):
        arrNew += [arrAll[i]]
    return arrNew

def buang_judul(arr):
    arrNew = []
    for i in range(1, length(arr)):
        arrNew += [arr[i]]
    return arrNew

def strip_enter(teks):
    result = ''
    i = 0
    while i <= (len(teks)-2):
        result += teks[i]
        i += 1
    return result

def border(tulisan, motif):
    tulisanpisah = tulisan.split('\n')
    kebawah = 2+len(tulisanpisah)
    sizetulisan = []
    for i in range(len(tulisanpisah)):
        sizetulisan.append(len(tulisanpisah[i]))
    kesamping = max(sizetulisan) + 10
    i = 0
    while i < kebawah:
        if i == 0 or i == kebawah - 1:
            print(motif * kesamping)
        else:
            if i in range(1,1+len(tulisanpisah)):
                print(str(motif)+' '*4+tulisanpisah[i-1]+' '*(4+max(sizetulisan)-len(tulisanpisah[i-1]))+str(motif))
            else:
                print(str(motif)+' '*(kesamping-2)+str(motif))
        i += 1










# # python ProsedurFungsi.py -f FolderFile

# buy_game()
# print("lagi")
# buy_game()



# id_user=3
# directory=loading()
# load(directory)
# print(data_game)
# print(user)
# print(kepemilikan)
# print(riwayat)
# # topup()  
# # print(user) 
# # print("@@@")
# # # buy_game()
# # # ubah_stok()
# # # tambah_game()
# list_game()
# list_game_toko(data_game)
# search_my_game()
# history(riwayat)
# register()
# print(user)
# help()

# print(data_game)
# print(user)
# print(kepemilikan)
# print(riwayat)
# print()
# border("Selamat datang di BNMO!", '#')


# Inisialisasi

data_game = []; user = []; kepemilikan = []; riwayat = []
commands = ['register', 'login', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 'search_game_at_store', 'topup', 'history', 'help', 'save', 'exit']
end = False
sudah_login = False
userkah = True

directory = loading()
# python f.py -f FolderFile
if directory != None:
    print("Loading data...")
    # load(directory)
    # print(data_game)
    # print(user)
    # print(kepemilikan)
    # print(riwayat)
    # print()
    border("Selamat datang di BNMO!", '#')

    while end == False:
        print(">>> ", end='')
        command = input()
        if command == "help":
            help()
        elif command == "login":
            if sudah_login == True:
                print("Anda sudah login sebelumnya. Jika Anda ingin login dengan akun lain, silakan exit terlebih dahulu. \n")
            else:
                sudah_login = login()
        elif command == "exit":
            end = exit()
        else:
            if sudah_login == True:
                if command == "register":
                    if userkah == True:
                        print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.\n")
                    else:
                        register()
                elif command == "tambah_game":
                    if userkah == True:
                        print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.\n")
                    else:
                        tambah_game()
                elif command == "ubah_game":
                    if userkah == True:
                        print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.\n")
                    else:
                        ubah_game()
                elif command == "ubah_stok":
                    if userkah == True:
                        print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.\n")
                    else:
                        ubah_stok()
                elif command == "list_game_toko":
                    list_game_toko(data_game)
                elif command == "buy_game":
                    if userkah == False:
                        print("Maaf, Anda harus menjadi user untuk melakukan hal tersebut.\n")
                    else:
                        buy_game()
                elif command == "list_game":
                    if userkah == False:
                        print("Maaf, Anda harus menjadi user untuk melakukan hal tersebut.\n")
                    else:
                        list_game()
                elif command == "search_my_game":
                    if userkah == False:
                        print("Maaf, Anda harus menjadi user untuk melakukan hal tersebut.\n")
                    else:
                        search_my_game()
                elif command == "search_game_at_store":
                    search_game_at_store(data_game)
                elif command == "topup":
                    if userkah == True:
                        print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.\n")
                    else:
                        topup()
                elif command == "history":
                    if userkah == False:
                        print("Maaf, Anda harus menjadi user untuk melakukan hal tersebut.\n")
                    else:
                        history(riwayat)
                elif command == "save":
                    save()
                else:
                    print("Maaf, perintah salah. \nBerikut list perintah yang dapat Anda gunakan.")
                    help()
            elif command in commands:
                print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”\n")
            else:
                print("Maaf, perintah tersebut tidak tersedia. Ketik 'help' untuk melihat list perintah.\n")
