module TesKategori where
    -- TES KATEGORI                         tesKategori (t, b, k)
    -- DEFINISI DAN SPESIFIKASI
    tesKategori :: Int -> Int -> Int -> Bool 
    {- tesKategori (t, b, k) menghasilkan nilai True jika orang dengan tinggi t dan berat b
    boleh menaiki kendaraan atraksi dengan kategori k sesuai dengan ketentuan di atas. Jika
    tidak boleh menaiki kategori apa pun, berarti nilai k = 0.
    Asumsi: 0 <= k <= 4, t > 0, b > 0 -}
    -- REALISASI
    tesKategori t b k
        | (t > 100 && b <= 150) = (k == 2 || k == 3 || k == 4)
        | (t <= 100 && b <= 150) = (k == 1)
        | (t <= 100 && b > 30 && b <= 150) = (k == 2)
        | (t <= 100 && b > 150) = (k == 2)
        | (t > 100 && t <= 200 && b > 150) = (k == 2 || k == 3)
        | otherwise = (k == 0)
    -- CONTOH APLIKASI
    -- tesKategori 120 80 1