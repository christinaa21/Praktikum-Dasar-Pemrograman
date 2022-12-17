module Pangkat where
    -- PANGKAT                                  pangkat(a, b)
    -- DEFINISI DAN SPESIFIKASI
    pangkat :: Int -> Int -> Int 
    {- pangkat(a,b) menerima masukan berupa dua buah integer, a dan b, dan
    mengembalikan hasil berupa a^b (a pangkat b). Asumsi: a > 0 dan b >= 0-}
    -- REALISASI
    pangkat a b
        | b == 0 = 1                      -- Basis
        | otherwise = a * pangkat a (b-1) -- Rekurens
    -- CONTOH APLIKASI
    -- pangkat 2 2
    -- 4
    -- pangkat 3 4
    -- 81