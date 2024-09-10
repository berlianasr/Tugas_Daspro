#user input
total = float(input("input total purchases: "))
student = input ("is the buyer a student? (y/n): ").lower() #lower utk mengecilkan huruf kapital

discountrate = 0.20
salestaxrate = 0.05

if(student == 'y'):
#jika pembeli adalah student
    discount = total*discountrate #harga diskon
    afterdisc = total - discount #harga stelah diskon
    salestax = salestaxrate*afterdisc #harga pajak
    finaltotal = afterdisc+salestax #harga stelah pajak
    print(f"Total purchases: ${total:.2f}")
    print(f"Student's discount (20%): {discount:.2f}")
    print(f"Discounted total: {afterdisc:.2f}")
    print(f"Sales tax (5%): {salestax}")
    print(f"Total: ${finaltotal:.2f}")

else:
#jika pembeli bukan student
    salestax = round(salestaxrate * total,2)    
    finaltotal = total+salestax
    print(f"Total purchase: ${total:.2f}")
    print(f"Sales tax (5%): {salestax:.2f}")
    print(f"Total: ${finaltotal:.2f}")