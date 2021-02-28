"""
Suatu segitiga mempunyai sisi dengan panjang berupa SA, SB dan SC. Berapa luas segitiga tersebut?
Penyelesaian :
Pertama-tama, tentukan dahulu posisi SA, SB, dan SC pada suatu segitiga.
Masukkan : SA, SB dan SC
keluaran : Luas
rumus menghitung luas segitiga : Luas = akar kuadrat s(s-SA)(s-SB)(s-SC)
dalam hal ini s berupa : s = (SA + SB + SC)/2
pseudokode :
Masukkan SA, SB dan SC
S <- (SA + SB + SC)/2
Luas <- akar (s * (s-SA) * (s-SB)*(s-SC))
tampilkan luas
"""
import math
SA = 30
SB = 45
SC = 25

s = (SA+SB+SC)/2
print(s)
luas = math.sqrt(50*(50-30)*(50-45)*(50-25))
print(luas)
luas_2 = math.sqrt(353.55)
print(luas_2)