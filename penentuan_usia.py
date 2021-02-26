"""
A dan B bersaudara. A lebih tua daripada B dengan selisih usia sebesar X tahun. usia A dan usia B adalah Y.
Berapa usia A dan B?
Penyelesaian :
Masukan : X dan Y
Keluaran : Usia A dan Usia B
dua persamaan yang didapat dari penjelasan tersebut berupa :
1. Usia A - Usia B = X
2. Usia A + Usia B = Y
Berdasarkan persamaan 1, didapatkan :
Usia A = X - Usia B
Berdasarkan persamaan 2, maka :
Usia A + Usia B = Y
2 * Usia B = X - Y
Dengan demikian,
Usia B = (X-Y)/2
pseukode :
masukkan X dan Y
Usia B <- (X-Y)/2
Usia A <- X - Usia B
Tampilkan Usia A dan Usia B
"""

x = 30
y = 20
usia_B = (x - y)/2
print(usia_B)

usia_A = x - usia_B
print(usia_A)