"""
cara menghitung penjumlahan :
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
Penyelesaian :
rumus : Jumlah = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
tidak ada masukan
Pseudokode :
Jumlah <- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
Tampilkan Jumlah
persoalan berbeda bila bilangan terakhir berupa suatu variabel, bentuknya menjadi :
1 + 2 + ... + (N-1) + N
N adalah masukan.
sehingga rumus menjadi :
Jumlah = (1+N) * (N/2)
penyelesaian :
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 adalah (1+10) * (10/2) = 55
Pseudokode :
Masukkan N
Jumlah <- (1+N) * (N/2)
Tampilkan Jumlah
"""
N = 10
jumlah = (1+N)*(N/2)
print(jumlah)