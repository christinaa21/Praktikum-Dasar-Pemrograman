module IsAllGanjil where
    -- IS ALL GANJIL                                isAllGanjil(l)
    -- DEFINISI DAN SPESIFIKASI
    isAllGanjil :: [Int] -> Bool 
    {- isAllGanjil(l) mengembalikan true apabila seluruh elemen l adalah bilangan ganjil.
    Fungsi mengembalikan true jika l adalah list kosong. -}
    isEmpty :: [Int] -> Bool 
    {- isEmpty(l) mengembalikan true jika list kosong. -}
    isEmpty l = null l
    -- Soal 1.
    -- REALISASI
    isAllGanjil l
        | isEmpty l = True
        | mod (head l) 2 == 0 = False 
        | otherwise = isAllGanjil (tail l)
    -- CONTOH APLIKASI
    -- isAllGanjil [7,3,9,13,15,31,19]
    -- True
    -- isAllGanjil [6,15,4,9]
    -- False
    -- isAllGanjil [9,15,27]
    -- True
    -- isAllGanjil []
    -- True