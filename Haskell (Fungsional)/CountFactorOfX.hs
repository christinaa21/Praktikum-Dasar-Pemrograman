module CountFactorOfX where
    -- COUNT FACTOR OF X                        -- countFactorOfX(n, l)
    -- DEFINISI DAN SPESIFIKASI
    countFactorOfX :: Int -> [Int] -> Int
    {- countFactorOfX n l mengembalikan banyaknya kemunculan bilangan
    yang merupakan faktor dari n pada l -}
    -- REALISASI
    countFactorOfX n l
        | null l = 0                                                                -- basis
        | head l == 0 = (countFactorOfX n (tail l))                                 -- rekurens
        | n < head l = (countFactorOfX n (tail l))                                  -- rekurens
        | (n >= head l) && (mod n (head l) /= 0) = (countFactorOfX n (tail l))      -- rekurens
        | (n >= head l) && (mod n (head l) == 0) = 1 + (countFactorOfX n (tail l))  -- rekurens
    -- CONTOH APLIKASI
    -- countFactorOfX 2 [1, 2, 3, 4]
    -- 2