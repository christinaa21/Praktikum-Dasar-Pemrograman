module LuasLayang where
    -- LUAS LAYANG               luasLayang(d1,d2)
    -- DEFINISI DAN SPESIFIKASI
    luasLayang :: Int -> Int -> Float 
    {- luasLayang (d1,d2) menghitung luas layang-layang berdasarkan diagonal 1
    dan diagonal 2. -}
    -- REALISASI
    luasLayang d1 d2 = 1/2 * fromIntegral (d1 * d2)
    -- CONTOH APLIKASI
    -- luasLayang 3 7
    -- 10.5