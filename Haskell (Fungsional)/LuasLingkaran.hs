module LuasLingkaran where
    -- LUAS LINGKARAN                           luasLingkaran (r)
    -- DEFINISI DAN SPESIFIKASI
    luasLingkaran :: Float -> Float 
    {- luasLingkaran (r) menghitung luas sebuah lingkaran berdasarkan rumus: Luas = 3.1415 * r * r
    dengan r = jari-jari sebuah lingkaran.
    Asumsi: r > 0 -}
    -- REALISASI
    luasLingkaran r = 3.1415 * r * r
    -- CONTOH APLIKASI
    -- luasLingkaran 2