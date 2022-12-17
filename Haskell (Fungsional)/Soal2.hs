-- JUMLAH DETIK         jumlahDetik(j,m,d)
-- DEFINISI DAN SPESIFIKASI
jumlahDetik :: Int -> Int -> Int -> Int
{- jumlahDetik(j,m,d) menghitung jumlah detik dari jam yang diinput
   pada j, m, d, dan dihitung mulai dari jam 0:0:0 pada tanggal yang sama.
   Asumsi: Jika j, m ,d yang diinput tidak valid, fungsi akan mengembalikan hasil berupa -1. -}
-- REALISASI
jumlahDetik j m d = if (j >= 0 && j <= 23) &&
                   (m >= 0 && m <= 59) &&
                   (d >= 0 && d <= 59)
                       then (j * 3600) + (m * 60) + d
                   else
                       (-1)
-- Contoh aplikasi
-- jumlahDetik 10 10 10