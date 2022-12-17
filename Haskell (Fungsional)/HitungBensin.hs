module HitungBensin where
    -- HITUNG BENSIN                hitungBensin(a, b)
    -- DEFINISI DAN SPESIFIKASI
    hitungBensin :: Int -> Int -> Int 
    {- hitungBensin(A, B) menghasilkan bilangan yang menunjukkan konsumsi bensin
    dari tiap-tiap kendaraan dari A sampai B. Kendaraan tersebut berangkat dari 
    posisi A sampai dengan posisi B.
    Asumsi: A <= B -}
    hitungJarak :: Int -> Int 
    {- hitungJarak(X) menghasilkan jumlah bensin yang diperlukan dari satu kendaraan
    dengan posisi awal tertentu. X = A -}
    -- REALISASI
    hitungBensin a b
        | a == b = hitungJarak a
        | otherwise = (hitungJarak a) + hitungBensin (a+1) b
    hitungJarak x
        | x == 1 = 0
        | mod x 2 == 0 = 1 + hitungJarak (div x 2)
        | otherwise = 1 + hitungJarak (3*x + 1)
    -- CONTOH APLIKASI
    -- hitungBensin 11 11
    -- 14
    -- hitungBensin 1 10
    -- 67