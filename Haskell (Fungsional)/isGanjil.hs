-- IsGanjil                                isGanjil(n)
-- DEFINISI DAN SPESIFIKASI
isGanjil :: Int -> Bool 
{- isGanjil(n) menghasilkan True jika n adalah bilangan ganjil,
dan menghasilkan False jika n adalah bilangan genap.
Asumsi: n >= 0 -}
-- REALISASI
isGanjil n
    | n <= 1    = n == 1
    | otherwise = isGanjil (n-2)
-- CONTOH APLIKASI
-- isGanjil 1