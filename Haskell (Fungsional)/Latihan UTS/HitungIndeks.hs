-- HITUNG INDEKS					hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes)
-- DEFINISI DAN SPESIFIKASI
hitungIndeks :: Float -> Float -> Float -> Int
{- hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes) menerima 3 input bertipe float yaitu nilaiUTS,
nilaiUAS, nilaiTubes dan mengeluarkan indeks mahasiswa (dinotasikan dengan bilangan bulat). 
Asumsi: input benar [0…100] -}
-- REALISASI
hitungIndeks nilaiUTS nilaiUAS nilaiTubes
	| (nilaiUTS == 0) || (nilaiUAS == 0) || (nilaiTubes == 0) = 0
	| (nilaiUTS > 0 && nilaiUTS < 40) || (nilaiUAS > 0 && nilaiUAS < 40) = 1
	| (nilaiUTS >= 40) && (nilaiUAS >= 40) && (nilaiTubes > 0 && nilaiTubes < 40) = 2
	| (nilaiUTS >= 40 && nilaiUTS < 75) && (nilaiUAS >= 40 && nilaiUAS < 75) && (nilaiTubes >= 40 && nilaiTubes < 75) = 2
	| (nilaiUTS >= 75) && (nilaiUAS >= 75) && (nilaiTubes >= 75) = 4
	| otherwise = 3
-- CONTOH APLIKASI
-- hitungIndeks 100 100 0
-- 0
-- hitungIndeks 100 100 20
-- 2
-- hitungIndeks 100 20 100
-- 1