-- LUAS BUJUR SANGKAR                       luasBS(s)
-- DEFINISI DAN SPESIFIKASI
luasBS :: Int -> Int
{- luasBS(s) menghitung luas bujur sangkat dengan panjang sisi s.
Asumsi: s > 0 -}
-- REALISASI
luasBS s = if s == 1 then 1
           else
               luasBS (s-1) + 2 * s - 1
-- CONTOH APLIKASI
-- luasBS 10