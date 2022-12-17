-- F DERET TUJUH LIST								fDeretTujuhList(d,e)
-- DEFINISI DAN SPESIFIKASI
fDeretTujuhList :: Int -> Int -> [Int]
{- fDeretTujuhList (d,e) menerima input berupa dua buah bilangan integer d dan e (asumsikan d > 0
dan e > 0), dan menghasilkan sebuah list bilangan integer yang berisi elemen ke-d hingga ke-e dari 
deret segitujuh. Jika e < d, dihasilkan list kosong. -}
-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
(list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li
-- REALISASI
fDeretTujuh :: Int -> Int
fDeretTujuh m
	| m == 1 = 1
	| otherwise = m + 4*(m-1) + fDeretTujuh (m-1)
fDeretTujuhList d e
	| e < d = []
	| otherwise = konso (fDeretTujuh d) (fDeretTujuhList (d+1) e)
-- CONTOH APLIKASI
-- fDeretTujuhList 2 4
-- [7,18,34]
-- fDeretTujuhList 3 3
-- [18]
-- fDeretTujuhList 4 3
-- []
