# Input populasi
populasi = int(input("Masukkan jumlah populasi komunitas: "))

# Asumsi yang diberikan
toilet_per_orang = 1 / 3  # Ada 1 toilet untuk setiap 3 orang
flush_per_hari = 14  # Toilet disiram rata-rata 14 kali per hari
liter_per_flush_tua = 15  # Toilet lama menggunakan 15 liter per siraman
liter_per_flush_baru = 2  # Toilet baru menggunakan 2 liter per siraman
biaya_per_toilet = 150  # Biaya untuk mengganti satu toilet baru adalah $150

# Menghitung jumlah toilet
jumlah_toilet = populasi * toilet_per_orang

# Menghitung penggunaan air per hari untuk toilet lama dan toilet baru
air_digunakan_toilet_lama = jumlah_toilet * flush_per_hari * liter_per_flush_tua
air_digunakan_toilet_baru = jumlah_toilet * flush_per_hari * liter_per_flush_baru

# Menghitung penghematan air harian
penghematan_air_harian = air_digunakan_toilet_lama - air_digunakan_toilet_baru

# Menghitung total biaya penggantian toilet
biaya_total_penggantian = jumlah_toilet * biaya_per_toilet

# Output hasil
print(f"Jumlah air yang dihemat per hari adalah {penghematan_air_harian:.2f} liter.")
print(f"Biaya total untuk mengganti semua toilet adalah ${biaya_total_penggantian:.2f}.")
