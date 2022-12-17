-- KONVERSI SUHU							konversiSuhu(t,k)
-- DEFINISI DAN SPESIFIKASI
konversiSuhu :: Float -> Char -> Float
{- konversiSuhu(t,k) mengkonversi suhu dari satu satuan Celcius ke satuan suhu lain, yaitu 
Fahrenheit, Reamur, atau Kelvin. -}
-- REALISASI
konversiSuhu t k
	| k == 'R' = (4/5) * t
	| k == 'F' = ((9/5) * t) + 32
	| k == 'K' = t + 273.15
-- CONTOH APLIKASI
-- konversiSuhu 25 'R'
-- 20
-- konversiSuhu 37 'F'
-- 98.6
-- konversiSuhu (-30) 'K'
-- 243.15
