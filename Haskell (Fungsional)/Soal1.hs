-- APAKAH JAM VALID?         isJamValid(j,m,d)
-- DEFINISI DAN SPESIFIKASI
isJamValid :: Int -> Int -> Int -> Bool 
{- isJamValid(j,m,d) menghasilkan nilai true jika j, m, d menyusun jam
    yang valid. Definisi jam yang valid adalah jika elemen jam (j)
    bernilai antara 0 dan 23, elemen menit (m) bernilai antara 0 dan 59,
    dan elemen detik (d) bernilai antara 0 dan 59. -}
-- REALISASI
isJamValid j m d = (j >= 0 && j <= 23) &&
                   (m >= 0 && m <= 59) &&
                   (d >= 0 && d <= 59)
-- Contoh aplikasi
-- isJamValid 23 10 10