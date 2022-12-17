module IsEqFront where
    -- IS EQ FRONT                      -- isEqFront(t1, t2)
    -- DEFINISI DAN SPESIFIKASI
    isEqFront :: [Char] -> [Char] -> Bool
    {- isEqFront(t1,t2) menghasilkan true jika potongan awal list t2 mengandung t1
    (dengan panjang dan urutan karakter yang sama). Banyaknya elemen t2 selalu >= t1. t1 & t2 tidak kosong -}
    isOneElement :: [Char] -> Bool
    {- isEmpty(l) true jika list elemen l hanya berisi 1 elemen.-}
    -- REALISASI
    isOneElement l = length l == 1
    isEqFront t1 t2
        | isOneElement t1 && (head t1 == head t2) = True  --basis
        | head t1 == head t2 = isEqFront (tail t1) (tail t2) -- rekurens
        | otherwise = False
    -- CONTOH APLIKASI
    -- isEqFront ['a','b','c'] ['a','b','c','d','e']
    -- True