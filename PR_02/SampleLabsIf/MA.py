# Membaca input
M, N, T = map(int, input().split())

# Durasi lampu lalu lintas
red_light = 20
yellow_light = 5
green_light = 60
cycle_length = red_light + yellow_light + green_light

# Hitung berapa banyak siklus penuh dalam waktu T
full_cycles = T // cycle_length
remaining_time = T % cycle_length

# Total waktu lampu hijau dalam waktu T
green_time = full_cycles * green_light
if remaining_time > red_light + yellow_light:
    # Jika ada sisa waktu yang melewati lampu merah dan kuning, hitung waktu hijau sisa
    green_time += min(green_light, remaining_time - red_light - yellow_light)

# Hitung berapa banyak mobil yang bisa melewati lampu lalu lintas
cars_passed = green_time // 5

# Mobil yang tersisa di depan setelah lampu hijau
cars_left_front = max(M - cars_passed, 0)

# Jika kamu bisa lewat (berarti semua mobil di depan sudah lewat)
if cars_passed >= M:
    print(f"YES! {max(N - (cars_passed - M), 0)}")  # Mobil di belakang tersisa
else:
    print(f"NO! {cars_left_front + N}")  # Mobil tersisa di depan dan belakang
