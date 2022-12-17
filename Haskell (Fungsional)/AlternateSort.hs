module AlternateSort where
    -- ALTERNATE SORT                      -- alternateSort(l)
    -- DEFINISI DAN SPESIFIKASI
    alternateSort :: [Int] -> [Int]
    {- alternateSort(l, f) menghasilkan list dengan ketentuan pada algoritma prosedural
    yang dibuat oleh Pak Engi. -}
    isEmpty :: [Int] -> Bool
    {- isEmpty(l) true jika list elemen l kosong.-}
    konso :: Int -> [Int] -> [Int]
    {- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
        dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
    isOneElmt :: [Int] -> Bool
    -- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
    minElem :: [Int] -> Int
    -- minElem l menghasilkan elemen terkecil dari list of integer.
    del :: Int -> [Int] -> [Int]
    -- del x l menghapus elemen x dari list l
    sort :: [Int] -> [Int]
    -- sort menghasilkan sebuah list of integer yang elemennya terurut dari terkecil ke terbesar.
    -- REALISASI
    isOneElmt l = (length l) == 1
    isEmpty l = null l
    konso e lc = [e] ++ lc
    minElem l
        | isOneElmt l = head l
        | otherwise = if head l < minElem (tail l) then head l else minElem (tail l)
    del x l
        | isEmpty l = []
        | x == head l = tail l
        | otherwise = konso (head l) (del x (tail l))
    sort l
        | isEmpty l = l
        | otherwise = konso (minElem l) (sort(del(minElem l) l))
    alternateSort l
        | isEmpty l || isOneElmt l = l
        | otherwise = konso (head (sort l)) (konso (last(sort l)) (alternateSort(init(tail(sort l)))))
    -- CONTOH APLIKASI
    -- alternateSort [9,10,11,12]
    -- [9,12,10,11]
    -- alternateSort [5,2,5,2,1]
    -- [1,5,2,5,2]