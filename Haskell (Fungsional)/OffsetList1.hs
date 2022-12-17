module OffsetList1 where
    -- OFFSET LIST                      -- offsetList(f, g, a, b)
    -- DEFINISI DAN SPESIFIKASI
    offsetList :: (Float -> Float) -> (Float -> Float) -> Float -> Float -> [Float]
    {- offsetList(f,g,a,b) menerima masukan dua buah fungsi, misalnya f dan g, serta dua
    buah bilangan riil (float), a dan b. Fungsi offsetList akan menghasilkan sebuah list
    of float yang merupakan penerapan fungsi f terhadap bilangan float antara a dan b,
    dimulai dari a dengan increment menggunakan fungsi g.-}

    -- DEFINISI DAN SPESIFIKASI PRIMITIF LIST
    -- KONSTRUKTOR
    konso :: Float -> [Float] -> [Float]
    {- konso e li menghasilkan sebuah list of float dari e dan li dengan e sebagai elemen pertama. -}
    konso e li = [e] ++ li

    -- DEFINISI DAN SPESIFIKASI FUNGSI CONTOH
    ide :: Float -> Float
    -- id x mengirimkan nilai x
    ide x = x
    p1 :: Float -> Float
    -- p1 x mengirimkan nilai x + 1
    p1 x = x + 1
    p2 :: Float -> Float
    -- p2 mengirimkan nilai x + 2
    p2 x = x + 2

    -- REALISASI
    offsetList f g a b
        | a > b = []                                        -- Basis
        | otherwise = konso (f a) (offsetList f g (g a) b)  -- Rekurens
    
    -- CONTOH APLIKASI
    -- offsetList ide p1 1.0 5.0
    -- [1.0,2.0,3.0,4.0,5.0]
    -- offsetList p1 p2 5.0 10.0
    -- [6.0, 8.0, 10.0]
    -- offsetList (\x -> x) (\x -> x + 2) 1.2 7.1
    -- [1.2,3.2,5.2]
    -- offsetList (\x -> if x < 0 then -999.0 else x + 3.2) (\x -> x + 0.5) (-1.0) 1.0
    -- [-999.0,-999.0,3.2,3.7,4.2]
    -- offsetList (\x -> x*x) (\x -> x + 1) 0.0 9.0
    -- [0.0,1.0,4.0,9.0,16.0,25.0,36.0,49.0,64.0,81.0]