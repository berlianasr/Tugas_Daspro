# Input kecepatan lepas landas dan jarak dari pengguna
kecepatan_lepas_kmh = float(input("Masukkan kecepatan lepas landas jet (km/jam): "))
jarak_m = float(input("Masukkan jarak akselerasi catapult (meter): "))

# Konversi kecepatan dari km/jam ke m/s
kecepatan_ms = kecepatan_lepas_kmh * (1000 / 3600)

# Hitung percepatan menggunakan rumus: a = v^2 / (2 * s)
percepatan = (kecepatan_ms ** 2) / (2 * jarak_m)

# Hitung waktu menggunakan rumus: t = v / a
waktu = kecepatan_ms / percepatan

# Tampilkan hasil
print(f"\nPercepatan: {percepatan:.2f} m/s²")
print(f"Waktu untuk mencapai kecepatan lepas landas: {waktu:.2f} detik")
