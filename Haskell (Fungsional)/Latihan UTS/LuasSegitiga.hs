-- LUAS SEGITIGA							luasSegitiga(a,t)
-- DEFINISI DAN SPESIFIKASI
luasSegitiga :: Float -> Float -> Float
{- luasSegitiga(a,t) menerima masukan 2 buah bilangan real (float) a dan t dengan a = alas segitiga
dan t = tinggi segitiga (asumsikan: a > 0, t > 0) dan menghasilkan luas segitiga dengan rumus:
luas = 1/2 * a * t -}
-- REALISASI
luasSegitiga a t = 1/2 * a * t
-- CONTOH APLIKASI
-- luasSegitiga 3 4
-- 6.0