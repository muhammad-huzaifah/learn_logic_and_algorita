"""
cara menghitung penjumlahan tanpa menggunakan rumus N(N+1)/2
1+2+...+(N-1)+N
Penyelesaian :
penjumlahan = 1+2+3+4+5+6...N
ada dua besaran yang dilibatkan dalam pengulangan perhitungan:
1. sebuah pencacah yang bergerak dari 1,2,3 hingga N
2. sebuah penampung hasil yang mula2 diisi dengan nol dan digunakan untuk menampung hasil penjumlahan  hasil sebelumnya dengan nilai pencacah.
Algoritma :
1. Masukkan N
2. mula2, jumlah diisi dengan 0
3. Atur agar pencacah bernilai 1
4. Lakukan pengulangan terhadap perintah2 berikut selama Pencacah <= N:
   a. Hitung jumlah + Pencacah kemudian simpan ke Jumlah kembali.
   b. Naikkan isi Pencacah sebesar 1
5. Tampilkan nilai Jumlah.
Pseudokode :
Masukkan N
Jumlah <- 0
Pencacah <- 1
Selama Pencacah <= N
    Jumlah <- Jumlah + Pencacah
    Pencacah <- Pencacah + 1
Akhir Selama
Tampilkan Jumlah
"""
N = 6
jumlah = 0,1,3,6,10,15
pencacah = 1,2,3,4,5
jumlah_pencacah = 1+2+3+4+5


print(jumlah_pencacah)

