jumlahsepatu = int(input("masukkan jumlah sepatu yang akan dikategorikan: "))

sepatukiri = [] #list untuk ukuran sepatu kiri
sepatukanan = [] #list untuk ukuran sepatu kanan

for i in range (jumlahsepatu): #agar pertanyaan ID dapat dijalankan sebanyak input jumlah sepatu
    idsepatu = input("masukkan ID sepatu: ") 
    ukuran = ''.join(filter(str.isdigit,idsepatu)) #mengeluarkan/mengambil hanya angka dari string ID sepatu 
    if 'R' in idsepatu:
        sepatukanan.append(ukuran) #jika terdapat 'R' dalam string ID maka ukuran akan dimasukkan kedalam list sepatu kanan 
    elif 'L' in idsepatu:
        sepatukiri.append(ukuran) #jika terdapat 'L' dalam string ID maka ukuran akan dimasukkan kedalam list sepatu kiri

jumlah_pasangan = 0 #jumlah pasangan awal adalah 0 shg ketika terdapat 1 pasangan akan mjd 1
# Looping untuk mengecek ukuran yang ada di sepatu kiri dan kanan
for ukuran in sepatukiri:
    if ukuran in sepatukanan: #untuk setiap ukuran di sepatu kiri, jika ukuran tsb juga ada di ukuran kanan,-
        jumlah_pasangan += 1 #maka jumlah pasangan bertambah 1

print(f"Jumlah pasangan sepatu: {jumlah_pasangan}")

"""
ukuran = ""
for c in idsepatu:
    if str.isdigit(c): ukuran += c
"""


"""
filter adalah fungsi bawaan Python yang digunakan untuk menyaring elemen-elemen dari sebuah iterable (dalam hal ini, string idsepatu).

str.isdigit adalah metode yang memeriksa apakah karakter adalah digit (angka). 
Jadi, filter(str.isdigit, idsepatu) akan menyaring semua karakter dari idsepatu dan hanya mengambil karakter yang berupa angka.

''.join(...) berfungsi untuk menggabungkan elemen-elemen hasil filter yang berupa angka menjadi satu string utuh. 
Dalam kasus ini, karena kita tidak memberikan pemisah ('' berarti tanpa pemisah), 
angka-angka tersebut digabungkan tanpa ada spasi atau karakter lain di antara mereka.
"""
