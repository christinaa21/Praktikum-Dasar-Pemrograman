module FilterList where
    -- FILTER LIST                      -- filterList(l, f)
    -- DEFINISI DAN SPESIFIKASI
    filterList :: [Int] -> (Int->Bool) -> [Int]
    {- filterList(l, f) melakukan filter atau penyaringan terhadap elemen list dan
    menghasilkan list baru dengan elemen yang lolos kriteria filter. -}
    isEmpty :: [Int] -> Bool
    {- isEmpty(l) true jika list elemen l kosong.-}
    konso :: Int -> [Int] -> [Int]
    {- konso(e,l) menghasilkan sebuah list dari e (sebuah elemen) dan l (list of elemen),
    dengan e sebagai elemen pertama: e o l -> l' -}
    isPos :: Int -> Bool 
    {- isPos(i) menghasilkan list baru yang hanya berisi elemen list masukan yang positif. -}
    isNeg :: Int -> Bool
    {- isNeg(i) menghasilkan list baru yang hanya berisi elemen list masukan yang negatif. -}
    isKabisat :: Int -> Bool
    {- isKabisat(i) menghasilkan list baru yang hanya berisi elemen list yang masuk kategori tahun kabisat. -}
    -- REALISASI
    isEmpty l = null l
    konso e l = [e] ++ l
    isPos i = i >= 0
    isNeg i = i < 0
    isKabisat i
        | mod i 100 == 0 = mod i 400 == 0
        | otherwise = mod i 4 == 0
    filterList l f
        | isEmpty l = []                                                          -- Basis
        | otherwise = if (f (head l)) then konso (head l) (filterList (tail l) f) -- Rekurens
                      else filterList (tail l) f
    -- CONTOH APLIKASI
    -- filterList [(-1), 2, 3, (-4)] isPos
    -- [2,3]
    -- filterList [(-1), 2, 3, (-4)] isNeg
    -- [-1,-4]
    -- filterList [2004,2003,2005,2012] isKabisat
    -- [2004,2012]
    -- filterList [(-1), 2, 3, (-4)] (\x -> x >= 0)
    -- [2,3]
    -- filterList [(-1), 2, 3, (-4)] (\x -> x < 0)
    -- [-1,-4]
    -- filterList [2004,2003,2005,2012] (\x -> (if mod x 100 == 0 then mod x 400 == 0 else mod x 4 == 0))
    -- [2004,2012]