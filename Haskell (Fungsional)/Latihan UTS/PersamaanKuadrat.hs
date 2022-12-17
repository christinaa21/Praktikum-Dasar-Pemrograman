-- PERSAMAAN KUADRAT						persamaanKuadrat(a,b,c,x)
-- DEFINISI DAN SPESIFIKASI
persamaanKuadrat :: Int -> Int -> Int -> Int -> Int
{- persamaanKuadrat(a,b,c,x) menerima 3 buah bilangan integer (a,b,c) dan sebuah nilai integer x,
menghasilkan nilai persamaan kuadrat dengan rumus: ax^2 + bx + c -}
-- REALISASI
persamaanKuadrat a b c x = (a*x*x) + (b*x) + c
-- CONTOH APLIKASI
-- persamaanKuadrat 1 2 1 (-1)
-- 0