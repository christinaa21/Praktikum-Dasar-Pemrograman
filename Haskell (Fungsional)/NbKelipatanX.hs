module NbKelipatanX where
    -- NbKelipatanX                     nbKelipatanX(m, n, x)
    -- DEFINISI DAN SPESIFIKASI
    nbKelipatanX :: Int -> Int -> Int -> Integer 
    {- nbKelipatanX(m, n, x) menghasilkan banyaknya bilangan kelipatan x di antara
    m dan n (m dan n termasuk) dengan menggunakan ekspresi rekursif.
    Bilangan y disebut kelipatan bilangan x, jika y habis dibagi dengan x.
    Prekondisi/syarat/asumsi yang berlaku adalah m <= n dan x <= n. -}
    -- REALISASI
    nbKelipatanX m n x
        | m == n && mod n x == 0 = 1
        | m == n && mod n x /= 0 = 0
        | m /= n && mod n x == 0 =
            1 + nbKelipatanX m (n-1) x
        | otherwise = nbKelipatanX m (n-1) x
    -- nbKelipatan X 1 1 1
    -- 1