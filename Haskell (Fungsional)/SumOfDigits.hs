module SumOfDigits where
    -- SumOfDigits               sumOfDigits(n)
    -- DEFINISI DAN SPESIFIKASI
    sumOfDigits :: Int -> Int
    {-sumOfDigits(n) menghasilkan penjumlahan setiap bilangan tunggal yang membentuk n positif
    Asumsi: n >= 0 -}
    sumOfDigitsPosNeg :: Int -> Int
    {- sumOfDigitsPosNeg(n) menghasilkan penjumlahan setiap bilangan tunggal yang membentuk n negatif
    Asumsu: n < 0 -}
    -- REALISASI
    sumOfDigits n =
        if n == 0 then 0
        else
            sumOfDigits(div n 10) + mod n 10
    sumOfDigitsPosNeg n =
        if n == 0 then 0
        else
            sumOfDigits(div (abs n) 10) + mod (abs n) 10
    -- CONTOH APLIKASI
    -- sumOfDigits 123
    -- 6
    -- sumOfDigitsPosNeg -45
    -- 9