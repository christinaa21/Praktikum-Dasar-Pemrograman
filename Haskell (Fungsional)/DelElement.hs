module DelElement where
    -- DEL ELEMENT                                delElement(x,l)
    -- DEFINISI DAN SPESIFIKASI
    delElement :: Int -> [Int] -> [Int]
    {- delElement(x,l) mengembalikan list l dengan elemen x yang telah dihapus dari l.
    Jika x bukan elemen l, maka fungsi mengembalikan l semula.
    Prekondisi: elemen l unik (setiap elemen hanya muncul 1 kali). -}
    isEmpty :: [Int] -> Bool 
    {- isEmpty(l) mengembalikan true jika list kosong. -}
    isEmpty l = null l
    konso :: Int -> [Int] -> [Int]
    {- konso(e,li) menghasilkan sebuah list of integer dari e dan li dengan e sebagai elemen pertamanya. -}
    konso e li = [e] ++ li
    -- Soal 3.
    -- REALISASI
    delElement x l
        | isEmpty l = l                                      -- Basis
        | x == head l = tail l
        | otherwise = konso (head l) (delElement x (tail l)) -- Rekurens
    -- CONTOH APLIKASI
    -- delElement 13 [7,3,9,13,15,31,19]
    -- [7,3,9,15,31,19]
    -- delElement 5 [6,15,4,9]
    -- [6,15,4,9]
    -- delElement 27 [9,15,27]
    -- [9,15]
    -- delElement 5 []
    -- []