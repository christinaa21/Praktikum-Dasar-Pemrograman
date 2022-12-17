-- LIST COUNT N 							 listCountN(l, n)
-- REALISASI
konso :: Int -> [Int] -> [Int]
    {- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
    (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
    -- REALISASI
konso e li = [e] ++ li

konsDot :: [Int] -> Int -> [Int]
    {- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
    e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
    -- REALISASI
konsDot li e = li ++ [e]

nbX :: [Int] -> Int -> Int 
{- nbX l x menghasilkan banyaknya kemunculan x di l -}
isEmpty :: [Int] -> Bool
    -- isEmpty l  true jika list of integer l kosong
    -- REALISASI
isEmpty l = null l

-- REALISASI
nbX l x
	| isEmpty l = 0
	| otherwise = if x == (head l) then 1 + nbX (tail l) x
		           else nbX (tail l) x
-- REALISASI
listCountN :: [Int] -> Int -> ([Int], Int)
listCountN l n
    | isEmpty l = ([], 0)
    | otherwise = ((konso (if nbX l (head l) == n then head l else listCountN (tail l) n) (listCountN (tail l) n)), (if nbX (head l) == n then 1 + (listCountN (tail l) n) else listCountN (tail l) n))
-- CONTOH APLIKASI
-- removeElmt [1,2,2,4,5,6,1,5,5,6,5,6] 2
-- ([1,2],2)
-- removeElmt [7] 7
-- ([1],1)
