-- APAKAH DATE VALID?         isDateValid(d,m,y)
-- DEFINISI DAN SPESIFIKASI
isDateValid :: Int -> Int -> Int -> Bool
{- isDateValid(d,m,y) mengembalikan nilai true jika d, m, y membentuk date
    yang valid. Definisi date yang valid adalah jika elemen hari (d)
    bernilai antara 1 dan 31, tergantung pada bulan dan apakah tahun kabisat
    atau bukan, elemen bulan (m) bernilai antara 1 dan 12,
    dan elemen tahun (y) bernilai antara 0 dan 99.
    Nilai y mewakili tahun 1900 s.d. 1999 -}
-- REALISASI
isDateValid d m y = ((y >= 0 && y <= 99) && (m >= 1 && m <= 12)) && (
                    if m == 2 then
                        if mod y 4 == 0 then (d >= 1 && d <= 29)
                        else (d >= 1 && d <= 28)
                    else if ((m == 4) || (m == 6) || (m == 9) || (m == 11)) then (d >= 1 && d <= 30)
                    else (d >= 1 && d <= 31))
-- Contoh aplikasi
-- isDateValid 23 10 10