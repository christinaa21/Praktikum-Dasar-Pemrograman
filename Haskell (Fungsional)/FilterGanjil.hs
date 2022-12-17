module FilterGanjil where
    -- FILTER GANJIL                      -- filterGanjil(li)
    -- DEFINISI DAN SPESIFIKASI
    filterGanjil :: [Int] -> [Int]
    {- filterGanjil(li) melakukan filtering terhadap sebuah list of integer li
    sehingga menghasilkan list dengan elemen yang hanya terdiri atas bilangan ganjil
    yang muncul di li. Asumsi: Semua elemen li adalah bilangan integer >= 0. li mungkin kosong. -}
    -- REALISASI
    filterGanjil li
        | null li = []                                    -- Basis
        | mod (head li) 2 == 0 = filterGanjil (tail li)   -- Rekurens
        | otherwise = [head li] ++ filterGanjil (tail li) -- Rekurens
    -- CONTOH APLIKASI
    -- filterGanjil [1, 2, 3, 4]
    -- [1, 3]