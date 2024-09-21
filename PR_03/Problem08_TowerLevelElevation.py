# N = lantai total
# M = energi awal
# X = lantai awal
# Y = lantai yg dituju
# A[i] = Energi tiap lantai ke-i
# E = kekurangan energi

N,M,K = map(int, input("input N,M,K: ").split( ))
A = list(map(int, input("masukkan energi yang dibutuhkan di tiap lantai: ").split())) #list energi tiap lantai

total_energi_dibutuhkan = 0 

for k in range (K):
    X,Y = map(int, input().split()) #lantai awal dan tujuan tiap kasus

    energi_dibutuhkan = 0

    for i in range (X-1, Y-1):
        energi_dibutuhkan += A[i] #menambahkan energi yang dibutuhkan pada lantai ke-i (yang nilainya diambil dari list A) ke variabel energi_dibutuhkan.

    total_energi_dibutuhkan += energi_dibutuhkan #energi yg dibutuhkan tiap kasus dimasukkan ke dalam total energi

if M >= total_energi_dibutuhkan: #sisa energi
    E = M - total_energi_dibutuhkan
else:
    E = (M - total_energi_dibutuhkan)*-1 #sisa energi *-1 agar tidak menghasilkan nilai negatif

if M >=total_energi_dibutuhkan:
    print(f"EZ banget, energiku sisa {E}!")
else:
    print(f"NT, kurang {E} energi sih")