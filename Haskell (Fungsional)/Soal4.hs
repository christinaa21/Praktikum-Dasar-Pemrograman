-- NILAI TENGAH         nilaiTengah(a,b,c)
-- DEFINISI DAN SPESIFIKASI
nilaiTengah :: Int -> Int -> Int -> Int
{- nilaiTengah(a,b,c) mengembalikan sebuah integer yang merupakan salah satu
   dari ke-3 nilai (a, b, dan c) yang jika diurutkan berada di tengah.
   a, b, dan c merupakan integer yang berlainan nilainya. -}
max3 :: Int -> Int -> Int -> Int
{- max3(a,b,c) menentukan maksimum dari 3 bilangan integer yang
   berlainan nilainya, a != b != c -}
min3 :: Int -> Int -> Int -> Int
{- min3(a,b,c) menentukan minimum dari 3 bilangan integer yang
   berlainan nilainya, a != b != c -}
-- REALISASI
nilaiTengah a b c
    | (a /= max3 a b c) && (a /= min3 a b c) = a
    | (b /= max3 a b c) && (b /= min3 a b c) = b
    | (c /= max3 a b c) && (c /= min3 a b c) = c
max3 a b c
    | (a>b) && (a>c) = a
    | (b>a) && (b>c) = b
    | (c>a) && (c>b) = c
min3 a b c
    | (a<b) && (a<c) = a
    | (b<a) && (b<c) = b
    | (c<a) && (c<b) = c
-- Contoh aplikasi
-- nilaiTengah 1 2 3