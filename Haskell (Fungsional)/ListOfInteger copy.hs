module ListOfInteger where
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

    
    -- Nb Occurence                                          -- nbOcc(l, x)
    -- DEFINISI DAN SPESIFIKASI
    nbOcc :: [Int] -> Int -> Int
    {- nbOcc(l,x) menerima masukan sebuah list of integer, misalnya l,
    dan sebuah integer, misalnya x, dan menghasilkan berapa banyak
    kemunculan x pada list of integer l. l mungkin kosong. -}
    -- REALISASI
    nbOcc l x
        | isEmpty l = 0             -- Basis
        | otherwise = if x == head l then 1 + nbOcc (tail l) x else nbOcc (tail l) x
    -- CONTOH APLIKASI
    -- nbOcc [] 10
    -- 0
    -- nbOcc [10] 10
    -- 1
    -- nbOcc [10,20,20] 20
    -- 2
    -- nbOcc [10,20,20] 3
    -- 0