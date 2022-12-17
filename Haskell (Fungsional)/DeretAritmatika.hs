module DeretAritmatika where
    -- DERET ARITMATIKA                     deretAritmatika(n, a, b)
    -- DEFINISI DAN SPESIFIKASI
    deretAritmatika :: Int -> Int -> Int -> Float 
    {- deretAritmatika(n, a, b) menghasilkan jumlah n suku pertama dari barisan
    aritmatika yang dapat disusun dengan komponen a dan b. Parameter a merupakan
    suku pertama dari suatu barisan aritmatika yang memiliki beda b. -}
    -- REALISASI
    deretAritmatika n a b = fromIntegral(n*(2*a + (n-1)*b))/ fromIntegral(2)
    -- CONTOH APLIKASI
    -- deretAritmatika 4 4 5
    -- 46