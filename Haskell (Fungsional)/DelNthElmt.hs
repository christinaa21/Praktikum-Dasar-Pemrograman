module DelNthElmt where
    -- Del Nth Elmt                        -- delNthElmt(n, l)
    -- DEFINISI DAN SPESIFIKASI
    delNthElmt :: Int -> [Char] -> [Char]
    {- delNthElmt(n,l) menghilangkan elemen ke-n dari l.
    Asumsi: n <= jumlah elemen l. l tidak kosong. -}
    -- REALISASI
    delNthElmt n l
        | n == 1 = tail l
        | otherwise = [head l] ++ delNthElmt (n-1) (tail l)
    -- CONTOH APLIKASI
    -- delNthElmt 2 [a, b, c, d]
    -- [a, c, d]