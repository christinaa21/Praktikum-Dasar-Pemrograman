module PersamaanKuadrat where
    -- PERSAMAAN KUADRAT               persamaanKuadrat(a, b, c, x)
    -- DEFINISI DAN SPESIFIKASI
    persamaanKuadrat :: Int -> Int -> Int -> Int -> Int 
    {- persamaanKuadrat (a,b,c,x) menghitung hasil persamaan kuadrat ax^2 + bx + c -}
    -- REALISASI
    persamaanKuadrat a b c x = a*(x^2) + b*x + c
    -- CONTOH APLIKASI
    -- persamaanKuadrat 1 2 1 (-1)
    -- 0