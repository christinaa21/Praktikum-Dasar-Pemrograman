-- JUMLAH DOLLAR DAN SEN         dollarSen(q,d,n,p)
-- DEFINISI DAN SPESIFIKASI
dollarSen :: Int -> Int -> Int -> Int -> (Int, Int)
{- dollarSen(q,d,n,p) menerima input sejumlah koin quarter, dime, nickel dan penny
   dan menghasilkan berapa dollar dan berapa sen yang senilai dengan total koin-koin tersebut. -}
cekTotalSen :: Int -> Int -> Int -> Int -> Int
{- cekTotalSen(q,d,n,p) menghitung total sen yang senilai dengan total koin-koin quarter,
   dime, nickel, dan penny (q, d, n, dan p) jika diubah menjadi sen. -}
-- REALISASI
dollarSen q d n p = (div (cekTotalSen q d n p) 100, mod (cekTotalSen q d n p) 100)
cekTotalSen q d n p = (q * 25) + (d * 10) + (n * 5) + p
-- Contoh aplikasi
-- dollarSen 10 11 12 13