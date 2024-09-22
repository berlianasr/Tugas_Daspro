x1, y1 = map(int, input().split( )) #titik pusat lingkaran
xs, ys = map(int, input().split( )) #titik awal raja
xf, yf = map(int, input().split( )) #titik akhir raja

jarak_sf = ((xf-xs)**2 + (yf-ys)**2)#jarak titik akhir dan awal raja
jarak_lf = ((xf-x1)**2 + (yf-y1)**2)#jarak titik akhir dan pusat lingkaran


if jarak_lf > jarak_sf:
    print("Yes") #memungkinkan tdk menyinggung lingkaran
    #karena jarak lingkaran ke titik akhir lebih jauh
else:
    print("No") #menyinggung lingkaran
    #karena jarak lingkaran ke titik akhir lebih dekat
