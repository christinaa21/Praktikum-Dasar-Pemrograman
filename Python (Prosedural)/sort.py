# Program Sorting
# Menerima input bilangan, misalnya N dan menerima N buah input bilangan yang disimpan di
# sebuah array. Kemudian, program mengurutkan bilangan dalam array tersebut dari besar ke kecil
# dengan menggunakan metode selection sort. Setelah itu, program menampilkan array yang telah
# diurutkan ke layar. Asumsi: input valid, yaitu bilangan integer dan N > 0.

# KAMUS
# N = integer
# arr = list

def get_max(arr, index_start):
# Mendapatkan maksimum array dari indeks indeks_start sampai selesai
    # KAMUS LOKAL
    # index_start, max, i = int
    max = arr[index_start]
    for i in range(index_start, len(arr)):
        if arr[i] >= max:
            max = arr[i]
    return max

def get_idx(arr, number):
# Mendapatkan index dari suatu angka dalam array
    # KAMUS LOKAL
    # number, i, index = int
    for i in range (len(arr)):
        if arr[i] == number:
            index = i
    return index

def swap(array, indeks_1, indeks_2):
# Swap elemen array indeks 1 dengan indeks 2
    # KAMUS LOKAL
    # array = list
    # indeks_1, indeks_2, Temp = int
    Temp = array[indeks_1]
    array[indeks_1] = array[indeks_2]
    array[indeks_2] = Temp

def sort(arr):
# Melakukan selection sorting.
    # KAMUS LOKAL
    # i, maxArr, maxIdx = int
  for i in range(len(arr)):
    maxArr = get_max(arr, i)
    maxIdx = get_idx(arr, maxArr)
    swap(arr, i, maxIdx)
  print(arr)

# ALGORITMA PROGRAM UTAMA
N = int(input())
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(input())
sort(arr)