t = int(input())  # banyak test case
output = []

for _ in range(t):
    n, k = map(int, input().split())  # banyak elemen array, ukuran subarray
    A = list(map(int, input().split()))  # elemen array A
    q = int(input())  # 1 untuk max, 2 untuk min

    if q == 1:
        max_sum = float('-inf')  #inisialisasi max_sum dengan negatif tak terhingga
        
        for length in range(1, k + 1): #cek mulai dari subbarray dgn 1 elemen
            current_sum = sum(A[:length])  # sum subarray pertama dengan panjang `length`
            max_sum = max(max_sum, current_sum) #membandingkan max_sum yang sudah ada dengan current_sum yang baru.
            
            # sliding window untuk mencari max sum subarray
            for i in range(length, n):
                current_sum += A[i] - A[i - length]
                max_sum = max(max_sum, current_sum)
        
        output.append(max_sum)  # tambahkan hasil ke list output sebagai integer
    
    elif q == 2:
        min_sum = float('inf')  # inisialisasi min_sum dengan tak terhingga
        
        for length in range(1, k + 1): #cek mulai dari subbarray dgn 1 elemen
            current_sum = sum(A[:length])  # sum subarray pertama dengan panjang `length`
            min_sum = min(min_sum, current_sum)
            
            # sliding window untuk mencari min sum subarray
            for i in range(length, n):
                current_sum += A[i] - A[i - length]
                min_sum = min(min_sum, current_sum)

        output.append(min_sum)  # tambahkan hasil ke list output sebagai integer

for x in output:
    print(x)
