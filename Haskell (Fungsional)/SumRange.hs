-- SUM RANGE                            sumRange(a, b)
-- DEFINISI DAN SPESIFIKASI
sumRange :: Int -> Int -> Int 
{- sumRange(a, b) menghasilkan penjumlahan semua bilangan dari a sampai dengan b.
Asumsi: a <= b, a >= 0, b >= 0 -}
-- REALISASI
sumRange a b =
    if a == b then a
    else
        sumRange a (b-1) + b
-- CONTOH APLIKASI
-- sumRange 2 2
-- 2
-- sumRange 2 4
-- 9