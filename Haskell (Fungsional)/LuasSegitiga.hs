module LuasSegitiga where
    -- LUAS SEGITIGA            luasSegitiga(a, t)
    -- DEFINISI DAN SPESIFIKASI
    luasSegitiga :: Float -> Float -> Float 
    {- luasSegitiga (a, t) menghitung luas segitiga berdasarkan rumus: Luas = 1/2 * a * t
    dengan a = alas segitiga dan t = tinggi segitiga.
    Asumsi: a > 0, t > 0 -}
    -- REALISASI
    luasSegitiga a t = 1/2 * a * t
    -- CONTOH APLIKASI
    -- luasSegitiga 10 12