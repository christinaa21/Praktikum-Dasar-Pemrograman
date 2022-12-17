prevDetik :: Int -> Int -> Int -> (Int, Int, Int)
prevDetik j m d =
	if d > 0 then (j, m, d-1)
	else
	       if m > 0 then (j, m-1, 59)
	       else
	              if j > 0 then (j-1, 59, 59)
	              else (23, 59, 59)