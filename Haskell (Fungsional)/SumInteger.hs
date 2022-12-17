module SumInteger where
    -- SUM INTEGER                      -- sumInteger(m, n, f)
    -- DEFINISI DAN SPESIFIKASI
    sumInteger :: Int -> Int -> (Int->Bool) -> Int
    {- sumInteger(m, n, f) menghasilkan penjumlahan dari semua integer antara m dan n (termasuk
    m dan n) yang memenuhi f. Jika dalam selang m dan n tidak ada yang memenuhi f, maka hasilnya adalah 0.
    Asumsi: m dan n merupakan bilangan ineger positif (>0). -}
    isGenap :: Int -> Bool 
    {- isGenap x menghasilkan true jika x adalah bilangan genap. -}
    gtThan5 :: Int -> Bool 
    {- gtThan5 x menghasilkan true jika x > 5. -}
    -- REALISASI
    isGenap x = mod x 2 == 0
    gtThan5 x = x > 5
    sumInteger m n f
        | m > n = 0
        | otherwise = if f n then n + sumInteger m (n-1) f else sumInteger m (n-1) f
    -- CONTOH APLIKASI
    -- sumInteger 2 9 isGenap
    -- 20
    -- sumInteger 2 9 gtThan5
    -- 30
    -- sumInteger 8 5 isGenap
    -- 0
    -- sumInteger 1 100 (\x -> mod x 100 == 0)
    -- 100
    -- sumInteger 1 100 (\x -> (mod x 2 == 0 && mod x 10 == 0) || (mod x 2 /= 0 && mod x 5 == 0))
    -- 1050
    -- sumInteger 25 25 (\x -> x < 10)
    -- 0