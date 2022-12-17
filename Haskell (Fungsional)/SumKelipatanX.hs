module SumKelipatanX where
    -- SUM KELIPATAN X                sumKelipatanX(m, n, x)
    -- DEFINISI DAN SPESIFIKASI
    sumKelipatanX :: Int -> Int -> Int -> Int 
    {- sumKelipatanX(m, n, x) menghasilkan jumlah total bilangan kelipatan x
    di antara m dan n (m dan n termasuk) dengan menggunakan ekspresi rekusrsif.
    Bilangan y disebut kelipatan bilangan x, jika y habis dibagi dengan x.
    Prekondisi/syarat/asumsi yang berlaku adalah m <= n dan x <= n. -}
    -- REALISASI
    sumKelipatanX m n x
        | m == n && mod n x == 0 = n
        | m == n && mod n x /= 0 = 0
        | m /= n && mod n x == 0 = n + sumKelipatanX m (n-1) x
        | otherwise = sumKelipatanX m (n-1) x
    -- CONTOH APLIKASI
    -- sumKelipatanX 1 1 1
    -- 1
    -- sumKelipatanX 1 10 2
    -- 30