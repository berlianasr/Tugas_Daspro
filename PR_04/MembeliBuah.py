N,K = map(int, input().split())#banyak buah, uang awal
A = list(map(int, input().split())) #harga buah
x = [] #banyak buah yg bs dibeli
for i in A:
    if i <= K:
        x.append(i) #masukkan buah yang bisa dibeii ke list x
print(len(x)) #banyaknya elemen yang ada dalam list x(banyaknya buah yang bisa dibeli)