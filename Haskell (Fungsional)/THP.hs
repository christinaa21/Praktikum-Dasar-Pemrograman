-- MENGHITUNG TAKE HOME PAY				thp(p, d)
-- DEFINISI DAN SPESIFIKASI
thp :: Bool -> Int -> Int
{- thp(p, d) menghitung THP yang akan diterima oleh seorang pegawai berdasarkan
masukan sebuah boolean (p) yang menyatakan kategori pegawai (bernilai True untuk
pegawai tetap dan False untuk pegawai kontrak) serta sebuah integer >= 0 (d) yang
menyatakan jumlah hari kerja pegawai tersebut. -}
-- REALISASI
thp p d
	| p && (d >= 15 && d <= 20) = 4000000 + 1000000
	| p && (d > 20) = 4000000 + 1000000 + (d-20)*100000
	| p && (d < 15) = d * 200000
	| not p && (d <= 20) = d * 150000
	| not p && (d > 20) = 20*150000 + (d-20)*175000
-- INGAT! Ga boleh tulis (p == True). Langsung aja p, karena mubazir!
-- CONTOH APLIKASI
-- thp True 25
-- 5500000
-- thp False 15
-- 2250000
