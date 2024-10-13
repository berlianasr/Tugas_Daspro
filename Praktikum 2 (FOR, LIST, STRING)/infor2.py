# Input jumlah angka
n = int(input())  # jumlah angka

# Input N angka
numbers = list(map(int, input().split()))

# Cari angka terbesar untuk mengetahui batas frekuensi
max_number = max(numbers)

# Inisialisasi array untuk menghitung frekuensi tiap angka
count = [0] * (max_number + 1)

# Hitung frekuensi kemunculan tiap angka
for num in numbers:
    count[num] += 1

# Cari modus (angka dengan frekuensi terbesar)
modus = -1
max_count = 0

for i in range(len(count)):
    if count[i] > max_count:  # Jika frekuensi lebih besar dari modus sebelumnya
        max_count = count[i]
        modus = i
    elif count[i] == max_count:  # Jika frekuensi sama, ambil angka yang lebih besar
        modus = max(modus, i)

# Cek apakah modus adalah bilangan prima
is_prime = True
if modus < 2:  # Bilangan 0 dan 1 bukan bilangan prima
    is_prime = False
else:
    for i in range(2, int(modus ** 0.5) + 1):
        if modus % i == 0:
            is_prime = False
            break

# Output hasil
print("Modus:", modus)
if is_prime:
    print("Prima")
else:
    print("Bukan Prima")
