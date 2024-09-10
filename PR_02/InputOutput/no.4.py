# Meminta input dari pengguna
dollar = float(input("Masukkan jumlah uang dalam US dollar: "))

# Konversi rate dari USD ke GBP
konversi_rate = 0.65

# Menghitung jumlah uang dalam British pounds
pound = dollar * konversi_rate

# Menampilkan hasil
print(f"Jumlah uang dalam British pounds adalah: {pound:.2f} GBP")
