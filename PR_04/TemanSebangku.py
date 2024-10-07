#input jumlah murid, baris, dan kolom
N, r, c = map(int, input().split())

#list untuk menyimpan posisi setiap siswa
posisi_siswa = []

#input posisi setiap siswa
for _ in range(N):
    nomor, baris, kolom = map(int, input().split())
    posisi_siswa.append([nomor, baris, kolom])
 
#untuk setiap siswa, cek siapa yang ada di kanan atau kiri
for i in range(1, N + 1):
    #cari baris dan kolom siswa ke-i
    for siswa in posisi_siswa:
        if siswa[0] == i:
            baris, kolom = siswa[1], siswa[2]
            break

#cek sebelah kiri atau kanan
    siswa_kiri = 0
    siswa_kanan = 0
    
    #menemukan siapa yang ada di kolom - 1 (kiri) dan kolom + 1 (kanan)
    for siswa in posisi_siswa:
        nomor, brs, klm = siswa 
        if brs == baris:
            if klm == kolom - 1:  # Sebelah kiri
                siswa_kiri = nomor
            elif klm == kolom + 1:  # Sebelah kanan
                siswa_kanan = nomor

    #output nomor siswa yang ada di kiri atau kanan, atau 0 jika tidak ada
    if siswa_kiri>0:
        print(siswa_kiri)
    elif siswa_kanan>0:
        print(siswa_kanan)
    else:
        print("0")