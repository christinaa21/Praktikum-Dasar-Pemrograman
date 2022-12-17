module DeretSegitiga where
   -- DERET SEGITIGA                      deretSegitiga(n)
   -- DEFINISI DAN SPESIFIKASI
   deretSegitiga :: Int -> Int 
   {- deretSegitiga(n) menghasilkan nilai bilangan ke-n pada deret segitiga.
   Deret segitiga adalah 1, 3, 6, 10, 15, ... 
   Prekondisi: n > 0 -}
   -- REALISASI
   deretSegitiga n = if n == 1 then 1
                     else
                        deretSegitiga (n-1) + n
   -- CONTOH APLIKASI
   -- deretSegitiga 1