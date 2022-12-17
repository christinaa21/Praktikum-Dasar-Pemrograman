module MergeList where
    mergeList :: [Int] -> [Int] -> [Int]
    isEmpty :: [Int] -> Bool 
    konso :: Int -> [Int] -> [Int]
    isEmpty l = null l
    konso e l = [e] ++ l
    mergeList li1 li2
        | isEmpty li1 && isEmpty li2 = []
        | isEmpty li1 && not (isEmpty li2) = li2
        | not (isEmpty li1) && isEmpty li2 = li1
        | otherwise =
            if head li1 <= head li2 then konso (head li1) (mergeList (tail li1) li2)
            else konso (head li2) (mergeList li1 (tail li2))