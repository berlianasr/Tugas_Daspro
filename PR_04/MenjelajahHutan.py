#input baris, kolom, banyak pergerakan
r, c, N = map(int, input().split())


#grid untuk petak emas
petak_emas = []
for g in range(r):
    emas = list(map(int, input().split()))
    petak_emas.append(emas)

#pergerakan (R, L, U, D)
move = list(input())

#posisi awal di (0,0) dan total emas yang didapat
posisi = [0, 0]  # [baris, kolom]
total_emas = petak_emas[0][0]  #emas dari petak awal langsung ditambahkan
petak_emas[0][0] = 0  #emas di petak awal sudah diambil

# Loop untuk setiap pergerakan
for m in move:
    if m == 'R':
        posisi[1] += 1  #pindah ke kanan (kolom(index ke-1) bertambah)
        if r-1<posisi[1] or posisi[1]<0:
            break
        else:
            total_emas += 3 + petak_emas[posisi[0]][posisi[1]]  # Tambah 3 dan emas di petak
            petak_emas[posisi[0]][posisi[1]] = 0  # Emas di petak tersebut sudah diambil

    elif m == 'L':
        posisi[1] -= 1  #pindah ke kiri (kolom berkurang)
        if r-1<posisi[1] or posisi[1]<0:
            break
        else:
            total_emas += petak_emas[posisi[0]][posisi[1]] - 2  # Kurangi 2 dan tambah emas di petak
            petak_emas[posisi[0]][posisi[1]] = 0  # Emas di petak tersebut sudah diambil

    elif m == 'U':
        posisi[0] -= 1  #pindah ke atas (baris berkurang)
        if c-1<posisi[0] or posisi[0]<0:
            break
        else:
            total_emas += 3 + petak_emas[posisi[0]][posisi[1]]  # Tambah 3 dan emas di petak
            petak_emas[posisi[0]][posisi[1]] = 0  # Emas di petak tersebut sudah diambil

    elif m == 'D':
        posisi[0] += 1  #pindah ke bawah (baris bertambah)
        if c-1<posisi[0] or posisi[0]<0:
            break
        else:
            total_emas += petak_emas[posisi[0]][posisi[1]] - 2  # Kurangi 2 dan tambah emas di petak
            petak_emas[posisi[0]][posisi[1]] = 0  # Emas di petak tersebut sudah diambil

print(total_emas)

if posisi[0]<0 or posisi[0]>r or posisi[1]<0 or posisi[1]>c:
    print ("gerakanmu salah bung!")
