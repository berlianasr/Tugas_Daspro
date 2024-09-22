
N,M = input("Masukkan 1 angka dan 1 kata(Aku/Kamu): ").split( ) #split N dan M

N=int(N) #N diubah menjadi integer


if M == "Aku":
        # Tangga ke kanan
    for i in range(1, N + 1): #mencetak sebanyak N baris
        if i % 2 == 1:
            print ("I U " * (i // 2) + "I" )
        else:
            print ("U I " * (i // 2))

        # ketika ganjil: I U
        # ketika genap: U I
        
elif M == "Kamu":
        # Tangga ke kiri
    for i in range (1, N+1):
        if i % 2 == 1:
            print (" "*((N-i)*2) + "I U " * (i // 2) + "I" )
        else:
            print (" "*((N-i)*2) +"I U " * (i // 2))
        # diberi spasi di depan sebanyak (N-i)*2













        
"""
elif M == "Dia":
    # Tangga ke kiri (terbalik)
    for i in range(N, 0, -1):
        if i % 2 == 1:
            print(" " * ((N - i) * 2) + "I U " * (i // 2) + "I")
        else:
            print(" " * ((N - i) * 2) + "I U " * (i // 2))

elif M == "Kita":
    for i in range (N,0,-1):
        if i % 2 == 1:
            print("I U " * (i//2) + "I")
        else:
            print ("U I " * (i//2))
"""