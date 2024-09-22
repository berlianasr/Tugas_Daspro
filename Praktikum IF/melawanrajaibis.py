U = int(input())
K = int(input())
M = int(input())

apK = ((K//2)* 5 * 500//100) #AP Knight 
apM = ((M//2)* 2 * 100//100) #AP Minion
#K//2 dan M//2 karena dibekukan separuh, lalu dikali HP//100(AP ucup per tebasan)


sisaU= U-(apK+apM)-(100 * (1000//100)) # HP awal dikurangi AP Knight, Minion, dan Raja

if sisaU >= 0:
    print (f"Yey! Ucup Menang! HP tersisa: {sisaU}")
else:
    print ("Yah! Ucup Meninggoy.")