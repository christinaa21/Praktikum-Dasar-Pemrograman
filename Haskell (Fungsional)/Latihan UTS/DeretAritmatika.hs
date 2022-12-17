-- DERET ARITMATIKA						deretAritmatika(n,a,b)
-- DEFINISI DAN SPESIFIKASI
deretAritmatika :: Int -> Int -> Int -> Float
{- deretAritmatika (n,a,b) menerima masukkan 3 nilai integer, yaitu n, a, dan b. a merupakan suku
pertama dari barisan aritmatika yang memiliki beda b. Fungsi ini akan menghasilkan jumlah n suku
pertama dari barisan aritmatika tersebut. -} 
-- REALISASI
deretAritmatika n a b = fromIntegral (n*(2*a + (n-1)*b))/ fromIntegral (2)
-- CONTOH APLIKASI
-- deretAritmatika 4 4 5
-- 46.0