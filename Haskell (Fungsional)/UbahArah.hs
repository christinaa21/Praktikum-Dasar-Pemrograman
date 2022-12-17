module UbahArah where
    -- UBAH ARAH                            ubahArah(s,r)
    -- DEFINISI DAN SPESIFIKASI
    ubahArah :: Int -> Int -> Int
    {- ubahArah(s,r) adalah fungsi yang menerima masukan dua buah integer
    s dan r yang merepresentasikan arah pergerakan dan besar perubahan arah yang
    akan dilakukan (dalam satu derajat). Fungsi mengembalikan arah pergerakan yang baru
    dalam range 0 s.d. 359, setelah s diputar sebesar r. -}
    -- REALISASI
    ubahArah s r
        | r >= 0 = if (s+r) >= 360 then
                        if mod (s+r) 360 == 0 then 0
                        else mod (s+r) 360
                   else s+r
        | otherwise = if (s+r) < 0 then
                        if (360 + (s+r)) >= 0 then 360 + (s+r)
                        else
                            if mod (abs(360 + (s+r))) 360 == 0 then 0
                            else 360 - mod (abs(360 + (s+r))) 360
                      else if mod (abs(s+r)) 360 == 0 then 0
                      else s+r
    -- CONTOH APLIKASI
    -- ubahArah 50 100
    -- 150
    -- ubahArah 350 100
    -- 90
    -- ubahArah 10 (-100)
    -- 270
    -- ubahArah 358 (-359)
    -- 359
    -- ubahArah 20 340
    -- 0
    -- ubahArah 0 (-40)
    -- 320