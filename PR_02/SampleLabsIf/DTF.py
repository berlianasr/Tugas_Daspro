# user input
jam_mulai, menit_mulai, detik_mulai = map(int, input("enter live stream time begin(GMT+2): ").split(":"))
jam_saat_ini, menit_saat_ini, detik_saat_ini = map(int, input("enter current hour(GMT+7): ").split(":"))

# Mengonversi waktu mulai ke zona GMT+7
jam_mulai += 5  # Karena dari GMT+2 ke GMT+7 ada perbedaan 5 jam

# Menangani waktu jika setelah dikonversi melebihi 24 jam
if jam_mulai >= 24:
    jam_mulai -= 24

# Mengonversi waktu ke detik
waktu_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
waktu_saat_ini = jam_saat_ini * 3600 + menit_saat_ini * 60 + detik_saat_ini
waktu_mulai2= waktu_mulai+10800

# Menghitung selisih waktu
selisih = waktu_mulai - waktu_saat_ini

# Jika selisih kurang dari atau sama dengan 0, berarti Ali telah melewatkan siaran langsung
if selisih >= 0:
# Konversi kembali selisih ke format HH:MM:SS
    jam = selisih // 3600
    menit = (selisih % 3600) // 60
    detik = selisih % 60
    print(f"event ke 1{jam:02}:{menit:02}:{detik:02}")

elif -10800 < selisih < 0:
    print("see you on the next Pear Event!")

else:
    jam = selisih // 3600
    menit = (selisih % 3600) // 60
    detik = selisih % 60
    print(f"event ke 2{jam:02}:{menit:02}:{detik:02}")
