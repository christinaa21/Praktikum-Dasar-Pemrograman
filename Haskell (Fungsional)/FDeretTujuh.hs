-- F DERET TUJUH								fDeretTujuh(m)
-- DEFINISI DAN SPESIFIKASI
fDeretTujuh :: Int -> Int
{- fDeretTujuh (m) menerima masukan sebuah integer m lebih besar dari nol (m > 0), dan 
menghasilkan bilangan integer yang menyatakan elemen ke-m pada pola bilangan deret segitujuh. -}
-- REALISASI
fDeretTujuh m
	| m == 1 = 1
	| otherwise = 2*m + 1 + fDeretTujuh (m-1)
-- CONTOH APLIKASI
-- fDeretTujuh 5
-- 55
-- fDeretTujuh 4
-- 34
