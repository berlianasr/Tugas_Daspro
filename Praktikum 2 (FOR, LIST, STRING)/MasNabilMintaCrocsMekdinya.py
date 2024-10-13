layka = [1,2,3,4,5]

N = int(input())
B = list(map(int, input().split( )))
hasil = 1
for i in range(N):
    for j in range(i + 1, N):
        xor_value = B[i] ^ B[j]  # XOR antara elemen ke-i dan ke-j
        if hasil == 0:
            break 
        else:
            hasil *= xor_value  # Kalikan hasil XOR ke hasil akhir

# Cetak hasil akhir
print(hasil) 