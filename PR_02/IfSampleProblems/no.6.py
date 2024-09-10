

#map map() dalam Python digunakan untuk menerapkan suatu fungsi ke setiap item-
#dari suatu iterable (seperti list, tuple, atau set) dan mengembalikan hasilnya dalam bentuk objek map. 
#Objek map ini bisa diubah menjadi tipe iterable lain seperti list, tuple, atau set.

# float() dengan tanda kurung: Memanggil fungsi float untuk satu argumen yang ingin dikonversi ke tipe float.
# float dengan koma dalam map(float, iterable): Tidak memanggil fungsi float langsung, 
# tetapi menunjukkannya sebagai referensi untuk diterapkan pada setiap elemen dalam iterable (misalnya daftar, tuple).

#string.split(separator, maxsplit) contoh : .split(',', 2)
#separator (opsional): Karakter atau string yang digunakan sebagai pemisah untuk memecah string. Jika tidak diberikan, pemisah defaultnya adalah spasi.
#maxsplit (opsional): Jumlah maksimum pemisahan yang akan dilakukan. Jika tidak diberikan, semua bagian dari string akan dipisahkan.

#jadi jika dari fungsi di bawah, map akan mengubah setiap elemen menjadi tipe float yang juga dipisahkan oleh split 

x, y = map(float, input("Enter the coordinate(x,y): ").split(','))

if x==0 and y == 0:
    position = "on the origin"

elif x == 0:
    position = "on the y-axis"

elif y == 0:
    position = "on the x-axis"

elif x>0 and y>0:
    position = "quadrant I"

elif x<0 and y>0:
    position = "quadrant II"

elif x<0 and y<0:
    position = "quadrant III"

elif x>0 and y<0:
    position = "quadrant IV"

print(f"({x,y}) is in {position}")