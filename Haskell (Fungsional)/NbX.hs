-- NB X 										nbX(l, x)
-- DEFINISI DAN SPESIFIKASI
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
-- CONTOH APLIKASI
-- nbX [1,2,3,4,5,1,2,2] 2
-- 3
-- nbX [1,2,3,4] 9
-- 0
