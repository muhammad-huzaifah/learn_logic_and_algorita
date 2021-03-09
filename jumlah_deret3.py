"""
cara menghitung penjumlah berikut :
1 + 1/2 + 1/3 + ... + 1/(N-1) + 1/N
penyelesaian :
solusi untuk penjumlahan serupa 1 + 2 + ... + (N-1) + N. perbedaan hanya pada operasi penjumlahan
Algoritma :
1. Masukkan N
2. Mula2 jumlah diisi dengan 1
3. Atur pencacah nilai 2
4. Lakukan pengulangan terhadap perintah2 berikut selama pencacah <= N :
   a. Hitung Jumlah + (1/Pencacah) simpan ke jumlah kembali
   b. Naikkan isi pencacah sebesar 1
5. Tampilkan jumlah
Pseudokode :
Masukkan N
Jumlah <- 1
Pencacah <- 2
Selama Pencacah <- N
    Jumlah <- Jumlah + 1 / Pencacah
    Pencacah <- Pencacah + 1
Akhir Selama
Tampilkan Jumlah

"""