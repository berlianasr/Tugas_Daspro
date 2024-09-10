# Konstanta
GRAVITASI = 9.80  # m/s^2
EFISIENSI = 0.90  # efisiensi 90%
KEPADATAN = 1000  # kg/m^3 (kepadatan air)

# Meminta input dari pengguna
tinggi = float(input("Masukkan tinggi bendungan (dalam meter): "))
aliran = float(input("Masukkan aliran air (dalam meter kubik per detik): "))

# Menghitung laju massa (kg/s)
laju_massa = aliran * KEPADATAN

# Menghitung kerja yang dilakukan per detik (dalam joule)
kerja_per_detik = laju_massa * GRAVITASI * tinggi

# Menghitung daya yang dihasilkan dalam watt
daya_dihasilkan_watt = kerja_per_detik * EFISIENSI

# Mengonversi daya dari watt ke megawatt
daya_dihasilkan_megawatt = daya_dihasilkan_watt / 1e6

# Menampilkan hasil
print(f"Daya yang dihasilkan adalah {daya_dihasilkan_megawatt:.2f} megawatt.")
