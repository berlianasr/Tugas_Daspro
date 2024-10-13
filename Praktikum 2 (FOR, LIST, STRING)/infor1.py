# Input jumlah siswa
n = int(input())  # jumlah siswa

# Input ID buah yang dipilih tiap siswa
fruit_ids = list(map(int, input().split()))

# Jika tidak ada siswa
if n == 0:
    print(-1)
else:
    # Inisialisasi array untuk menghitung frekuensi tiap buah (ID 1-10)
    count = [0] * 11  # Buah bernomor ID dari 1 hingga 10

    # Hitung frekuensi kemunculan tiap buah
    for fruit in fruit_ids:
        count[fruit] += 1

    # Cari buah dengan frekuensi tertinggi
    max_fruit = -1
    max_count = 0
    tie = False

    for i in range(1, 11):  # Loop dari ID buah 1 sampai 10
        if count[i] > max_count:
            max_count = count[i]
            max_fruit = i
            tie = False
        elif count[i] == max_count:  # Jika ditemukan frekuensi yang sama
            tie = True

    # Jika ada seri
    if tie:
        print(-1)
    else:
        # Hitung jumlah buah yang perlu diubah agar semua sesuai dengan mayoritas
        changes_needed = n - max_count
        print(max_fruit)
        print(changes_needed)
