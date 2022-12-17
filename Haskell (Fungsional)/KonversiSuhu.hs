module KonversiSuhu where
    -- KONVERSI SUHU                    konversiSuhu (t, k)
    -- DEFINISI DAN SPESIFIKASI
    konversiSuhu :: Float -> Char -> Float 
    {- konversiSuhu (t, k) mengkonversi suhu dari satuan Celcius ke satuan suhu yang lain,
    yaitu Fahrenheit, Reamur, atau Kelvin. Dalam fungsi ini, t = besaran suhu dalam derajat C
    dan k = kode satuan suhu konversi yang diasumsikan bernilai 'R' (Reamur), 'F' (Fahrenheit),
    atau 'K' (Kelvin). -}
    -- REALISASI
    konversiSuhu t k = if k == 'R' then
                           4/5 * t
                       else if k == 'F' then
                           (9/5 * t) + 32
                       else -- k == 'K'
                           t + 273.15
    -- CONTOH APLIKASI
    -- konversiSuhu 25 'R'