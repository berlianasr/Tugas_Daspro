# Input
n, d1, d2, d3, d4 = map(int, input("enter jumping distance: ").split())

# Mengecek setiap jarak antara pilar apakah lebih besar dari panjang lompatan maksimal B
# lompatan maksimal B adalah n
if d1 > n:
    print("NO HE CAN'T")
elif d2 > n:
    print("NO HE CAN'T")
elif d3 > n:
    print("NO HE CAN'T")
elif d4 > n:
    print("NO HE CAN'T")
else:
    print("YES HE CAN")
