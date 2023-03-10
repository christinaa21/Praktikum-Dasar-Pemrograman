module HappyFive where
    -- DEFINISI DAN SPESIFIKASI LIST
    {- type List of Int: [ ] atau [e o List] atau [List o e]  
        Definisi type List of Int
        Basis: List of Int kosong adalah list of Int 
        Rekurens: 
        List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
        sebuah list atau
        dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

    -- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    konso :: Int -> [Int] -> [Int]
    {- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
        (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
    -- REALISASI
    konso e li = [e] ++ li

    konsDot :: [Int] -> Int -> [Int]
    {- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
        e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
    -- REALISASI
    konsDot li e = li ++ [e]

    -- DEFINISI DAN SPESIFIKASI SELEKTOR
    -- head :: [Int] -> Int
    -- head l menghasilkan elemen pertama list l, l tidak kosong

    -- tail :: [Int] -> [Int]
    -- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

    -- last :: [Int] -> Int
    -- last l menghasilkan elemen terakhir list l, l tidak kosong

    -- init :: [Int] -> [Int]
    -- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

    -- DEFINISI DAN SPESIFIKASI PREDIKAT
    isEmpty :: [Int] -> Bool
    -- isEmpty l  true jika list of integer l kosong
    -- REALISASI
    isEmpty l = null l

    isOneElmt :: [Int] -> Bool
    -- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
    -- REALISASI
    isOneElmt l = (length l) == 1


    -- HAPPY FIVE                      -- happyFive(l)
    -- DEFINISI DAN SPESIFIKASI
    happyFive :: [Int] -> [Int]
    {- happyFive(l) membuang setiap angka yang tidak berhubungan dengan 5 atau kelipatan dari
    5 dari sebuah list of integer. Angka di dalam list hanya bernilai satuan atau puluhan. -}
    -- REALISASI
    happyFive l
        | isEmpty l = []
        | (mod (head l) 5 == 0) || (mod (head l) 10 == 5) || (div (head l) 10 == 5) = konso (head l) (happyFive (tail l))
        | otherwise = happyFive (tail l)
    -- CONTOH APLIKASI
    -- happyFive [1, 2, 7, 5, 15, 17, 13, 14, 21, 20, 51, 52]
    -- [5, 15, 20, 51, 52]
    -- happyFive []
    -- []