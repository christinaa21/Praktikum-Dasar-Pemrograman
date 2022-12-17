module Kinerja where
    -- KINERJA                          kinerja(j, m, d)
    -- DEFINISI DAN SPESIFIKASI
    kinerja :: Int -> Int -> Int -> (Int, Int, Int, Int)
    {- kinerja(j, m, d) menghasilkan sebuah tuple (j, m, d, s) dengan penjelasan sebagai berikut:
    - j, m, d mewakili durasi antara jam selesainya pekerjaan karyawan dengan standar jam selesai
    (standar jam selesai = 17:30:00) berupa nilai dalam jam, menit, dan detik.
    - s mewakili status kinerja karyawan dengan keterangan nilai: 0 = tepat waktu, 1 = lebih awal,
    -1 = terlambat.
    Asumsi: Masukan selalu berupa integer positif dan pasti valid merepresentasikan jam sesuai definisi di atas.-}
    -- Fungsi Antara
    cekDurasi :: Int -> Int -> Int -> Int
    {- cekDurasi(j, m, d) menghasilkan selisih jumlah detik antara jam selesai bekerja dan standar
    jam selesai bekerja. Asumsi: sama seperti fungsi kinerja. -}
    jam :: Int -> Int -> Int -> Int
    {- jam(j, m, d) mengkonversi hasil cekDurasi ke jam -}
    sisaDetik :: Int -> Int -> Int -> Int
    {- sisaDetik(j, m, d) menghitung sisa detik setelah dikonversi ke jam -}
    menit :: Int -> Int -> Int -> Int
    {- menit(j, m, d) mengkonversi sisaDetik ke menit -}
    detik :: Int -> Int -> Int -> Int
    {- detik(j, m, d) menghitung sisa detik setelah dikonversi ke menit -}
    -- REALISASI
    kinerja j m d = (jam j m d, menit j m d, detik j m d,
                     if cekDurasi j m d < 0 then -1
                     else if cekDurasi j m d == 0 then 0
                     else 1)
    cekDurasi j m d = ((17 * 3600) + (30 * 60)) - ((j * 3600) + (m * 60) + d)
    jam j m d = div (abs(cekDurasi j m d)) 3600
    sisaDetik j m d = abs(cekDurasi j m d) - (jam j m d * 3600)
    menit j m d = div (sisaDetik j m d) 60
    detik j m d = sisaDetik j m d - (menit j m d * 60)
    -- CONTOH APLIKASI
    -- kinerja 17 0 0
    -- (0,30,0,1)