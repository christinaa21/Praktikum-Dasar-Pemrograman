-- FUNGSI KUADRAN					fungsiKuadran(x,y)
-- DEFINISI DAN SPESIFIKASI
fungsiKuadran :: Int -> Int -> String 
{- fungsiKuadran(x,y) menghasilkan kuadran dari titik x dan y yang diinput pada fungsi. -}
-- REALISASI
fungsiKuadran x y
	| (x >= 0) && (y >= 0) = "Kuadran 1"
	| (x < 0 ) && (y >= 0) = "Kuadran 2"
	| (x < 0) && (y < 0) = "Kuadran 3"
	| (x >= 0) && (y < 0) = "Kuadran 4"
-- CONTOH APLIKASI
-- fungsiKuadran 0 0
-- 1
-- fungsiKuadran -3 0
-- 2
