module UkuranBaju where
    -- UKURAN BAJU                      ukuranBaju (t, b)
    -- DEFINISI DAN SPESIFIKASI
    ukuranBaju :: Int -> Int -> Int 
    {- ukuranBaju (t, b) menghasilkan kode ukuran baju (1 = M, 2 = L, 3 = XL)
    atau kode 4 adalah untuk yang tidak mendapatkan kaos. Ukuran ini ditentukan
    dengan kondisi2 tertentu yang ditinjau berdasarkan masukan t (tinggi badan dalam cm)
    dan b (berat badan dalam kg).
    Asumsi: t > 0, b > 0-}
    -- REALISASI
    ukuranBaju t b
        | t <= 150 = 1
        | t > 170 && (b > 60 && b <= 80) = 3
        | (t > 150 && t <= 170) && (b <= 80) = 2
        | (t > 150 && t <= 170) && (b > 80) = 3
        | t > 170 && b <= 60 = 2
        | otherwise = 4
    -- CONTOH APLIKASI
    -- ukuranBaju 160 75