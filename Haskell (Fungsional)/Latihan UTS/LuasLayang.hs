-- LUAS LAYANG							layang(d1,d2)
-- DEFINISI DAN SPESIFIKASI
layang :: Int -> Int -> Float
{- layang (d1,d2) menerima masukan 2 nilai integer, yaitu kedua diagonal sebuah layang-layang
misalnya d1 dan d2. Realisasi fungsi layang akan menghasilkan luas layang-layang dengan rumus:
1/2*d1*d2 -}
-- REALISASI
layang d1 d2 = fromIntegral (d1*d2)/ fromIntegral (2)
-- CONTOH APLIKASI
-- layang 3 7
-- 10.5
