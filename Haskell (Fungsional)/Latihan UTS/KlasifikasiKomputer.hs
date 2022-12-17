-- KLASIFIKASI KOMPUTER						klasifikasi(c, g, h)
-- DEFINISI DAN SPESIFIKASI
klasifikasi :: Int -> Int -> Int -> Int
{- klasifikasi (c,g,h) menerima integer c (kemampuan CPU), g (kemampuan GPU), dan h
(kemampuan harddisk) untuk diklasifikasikan. -}
-- REALISASI
klasifikasi c g h
	| (c < 2) || (g < 2) || (h < 2) = 1
	| (c >= 2 && c < 5) || (g >= 2 && g < 5) = 2
	| (c >= 5 && c <= 7) && (g >= 5 && g <= 7) && (h >= 2 && h <= 7) = 3
	| (c > 7) && (g > 7) && (h > 7) = 5
	| otherwise = 4
-- CONTOH APLIKASI
-- klasifikasi 2 5 7
-- 2