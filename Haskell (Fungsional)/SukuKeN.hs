-- MENENTUKAN SUKU KE-N					sukuKeN(n)
-- DEFINISI DAN SPESIFIKASI
sukuKeN :: Int -> Int
{- sukuKeN(n) menghasilkan suku ke-n dari barisan 1, -4, 7, -10, 13, ….
dengan menggunakan rumus Un = a + b * (n-1). a = suku pertama dan b = beda.
Asumsi: n >= 1 -}
-- REALISASI
sukuKeN n =
	if (mod n 2) == 0 then (1 + 3*(n-1))*(-1)
	else (1 + 3*(n-1))
-- CONTOH APLIKASI
-- sukuKeN 8
-- (-22)