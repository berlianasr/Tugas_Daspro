import math

def is_prime(n, divisor):
    # jika divisor lebih besar dari √n, maka n adalah bilangan prima
    if divisor > int(math.sqrt(n)):
        return True
    # Jika n dapat dibagi habis oleh divisor, maka n bukan bilangan prima
    if n % divisor == 0:
        return False
    # Rekursi untuk memeriksa pembagi berikutnya
    return is_prime(n, divisor + 1)

# Input integer n
n = int(input("enter the number: "))

# Cek bilangan prima: mulai dengan divisor 2
if n > 1 and is_prime(n, 2):
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")
