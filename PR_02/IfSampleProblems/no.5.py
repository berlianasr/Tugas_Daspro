n = float(input("input data usage in Gbs: "))

if (0.0<n<=1.0):
    charges = 250
elif (1.0<n<=2.0):
    charges = 500
elif (2.0<n<=5.0):
    charges = 1000
elif (5.0<n<=10.0):
    charges = 1500
elif (10.0<n):
    charges = 2000
else:
    charges = None #jika data yang dimasukkan <=0
    print ("Bad data: data usage must be greater than 0")

if charges is not None:
    print (f"Charges for {n} Gbs: ${charges}")