module HitungIndeks where
    -- HitungIndeks               hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes)
    -- DEFINISI DAN SPESIFIKASI
    hitungIndeks :: Float -> Float -> Float -> Integer 
    {- hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes) menghasilkan indeks mahasiswa
    yang dinotasikan dengan bilangan bulat (A = 4, B = 3, dst sampai E = 0)
    Asumsi: input benar [0...100] -}
    -- REALISASI
    hitungIndeks nilaiUTS nilaiUAS nilaiTubes =
        if (nilaiUTS > 0) && (nilaiUAS > 0) && (nilaiTubes > 0) then
            if nilaiTubes < 40 then 2
            else
                if (nilaiUTS < 40) || (nilaiUAS < 40) then 1
                else
                    if (nilaiUTS < 75) && (nilaiUAS < 75) && (nilaiTubes < 75) then 2
                    else if (nilaiUTS >= 75) && (nilaiUAS >= 75) && (nilaiTubes >= 75) then 4
                    else 3
        else 0
    -- CONTOH APLIKASI
    -- hitungIndeks 100 100 0
    -- 0