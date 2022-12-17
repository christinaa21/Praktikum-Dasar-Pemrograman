module SumIsList where
    -- SUM IS LIST                       -- sumIsList(l)
    -- DEFINISI DAN SPESIFIKASI
    sumIsList :: [Int] -> Int
    {- sumIsList(l) menghitung hasil penjumlahan dari seluruh elemen sebuah
    list of integer l yang tidak kosong. -}
    isEmpty :: [Int] -> Bool
    {- isEmpty(l) true jika list elemen l kosong.-}
    -- REALISASI
    isEmpty l = null l
    sumIsList l
        | isEmpty l = 0                            -- basis
        | otherwise = head l + sumIsList (tail l)  -- rekurens
    -- CONTOH APLIKASI
    -- sumIsList [1, 2, 3, 4]
    -- 10