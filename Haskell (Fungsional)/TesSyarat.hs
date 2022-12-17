module TesSyarat where
    -- TES SYARAT                       tesSyarat(ip, pot)
    -- DEFINISI DAN SPESIFIKASI
    tesSyarat :: Float -> Float -> Int 
    {- tesSyarat(ip, pot) menghasilkan kategori beasiswa bernilai (0...4) yang berhak
    didapatkan oleh mahasiswa sesuai ketentuan di atas (jika kategori 0, berarti mahasiswa
    tersebut tidak berhak atas beasiswa. ip = IP mahasiswa dan pot = pendapatan orang tua
    Asumsi: 0 <= ip <= 4, pot >= 0 -}
    -- REALISASI
    tesSyarat ip pot
        | ip >= 3.5 = 4
        | pot < 1 && ip < 3.5 = 1
        | pot >= 1 && pot < 5 && ip < 3.5 && ip >= 2 = 3
        | pot >= 1 && pot < 5 && ip < 3.5 && ip < 2 = 2
        | otherwise = 0
    -- CONTOH APLIKASI
    -- tesSyarat 3.51 1.5