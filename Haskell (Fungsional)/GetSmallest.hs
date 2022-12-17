module GetSmallest where
    -- GET SMALLEST                                     getSmallest(l)
    -- DEFINISI DAN SPESIFIKASI
    getSmallest :: [Int] -> Int
    {- getSmallest(l) mengembalikan elemen terkecil di l. Prekondisi: l tidak kosong. -}
    isOneElmt :: [Int] -> Bool 
    {- isOneElmt(l) mengembalikan true jika hanya ada 1 elemen pada list l. -}
    isOneElmt l = length l == 1
    konsDot :: [Int] -> Int -> [Int]
    {- konsDot(e,li) menghasilkan sebuah list of integer dari e dan li dengan e sebagai elemen terakhir.-}
    konsDot li e = li ++ [e]
    -- Soal 2.
    -- REALISASI
    getSmallest l
        | isOneElmt l = head l
        | head l >= head (tail l) = getSmallest (tail l)
        | otherwise = getSmallest (konsDot (tail l) (head l))
    -- CONTOH APLIKASI
    -- getSmallest [7,3,9,13,15,31,19]
    -- 3
    -- getSmallest [6,15,4,9]
    -- 4
    -- getSmallest [9,15,27]
    -- 9