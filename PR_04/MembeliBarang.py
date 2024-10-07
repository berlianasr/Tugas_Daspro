N,M = map(int, input().split()) #jumlah barang dan jumlah lembar uang
P= list(map(int, input().split())) #harga barang
C= list(map(int, input().split())) #nominal uang

hargamax= 0
uangmin = 0
#ambil P positif dan C negatif agar harga max dan uang min
for i in P:
    if i > 0:
        hargamax += i
if hargamax == 0:
    hargamax = max (P)

for j in C:
    if j < 0:
        uangmin += j
if uangmin == 0:
    uangmin = min (C)
    
utang = (hargamax-uangmin)*-1
print (utang)


"""baris pertama diambil yang positif"""
"""yang kedua diambil negatif"""