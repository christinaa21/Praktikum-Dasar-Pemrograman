module ListIndex where
    -- LIST INDEX                      -- listIndex(l, f)
    -- DEFINISI DAN SPESIFIKASI
    listIndex :: [Int] -> (Int->Char) -> [Char]
    {- listIndex(l, f) menerima masukan sebuah list of integer, misalnya l dan
    sebuah fungsi yang menerima masukan sebuah integer dan menghasilkan sebuah char,
    misal f. Kemudian akan menghasilkan sebuah list of character yang melambangkan
    nilai-nilai indeks dari suatu list nilai integer. -}
    isEmpty :: [Int] -> Bool
    {- isEmpty(l) true jika list elemen l kosong.-}
    konso :: Char -> [Char] -> [Char]
    {- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
        dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
    -- REALISASI
    isEmpty l = null l
    konso e lc = [e] ++ lc
    listIndex l f
        | isEmpty l = []
        | otherwise = konso (f (head l)) (listIndex (tail l) f)
    -- CONTOH APLIKASI
    -- listIndex [75, 90, 10, 20, 100] (\x -> if x <= 100 && x > 80 then 'A' else if x <= 80 && x > 70 then 'B' else if x <= 70 && x > 65 then 'C' else if x <= 65 && x > 55 then 'D' else 'E')
    -- ["BAEEA"]