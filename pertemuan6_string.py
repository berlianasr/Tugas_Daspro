#create string
string0 = "Berliana Sarlita Rahajeng"
string1 = "5054241023"
string2 = "Surabaya"

#print string
print("Nama saya adalah " + string0)
print("NRP " + string1)
print("Asal daerah " + string2)

#access in string
print("Inisial saya " + string0[0]+string0[9]+string0[17])

#string slicing
print("Nama belakang saya "+ string0[-8:])#bisa juga [17:]
print("Nama panggilan saya " + string0[-5:])#bisa juga [20:]

x = "saya mahasiswa RKA"
print(x)
newx = x[:4] + " bukan " + x[4:14] + " RPL"
#          "saya"              "mahasiswa"
print(newx)

"###################################################"
#TUGAS IMPLEMENTASI
print ("\nTUGAS IMPLEMENTASI STRING")
#1 Deleting a character dari kota asal
string2 = list(string2)
del string2[0]
kota = ''.join(string2)
print("\nDeleting a character dari kota asal: ")
print(kota)

#2. Escape Sequencing in Python + Example

a = '''He's the "Mr.X"'''
print("\nInitial string with use of Triple Quotes: ")
print(a)

a = 'He\'s the "Mr.X"'
print("\nEscaping single Quote: ")
print(a)

a = "He's the \"Mr.X\""
print("\nEscaping double quotes:")
print(a)

b = "C:\\Users\\ACER\\OneDrive - Institut Teknologi Sepuluh Nopember"
print("\nEscaping backslashes:")
print(b)

# Printing Paths with the
# use of Tab
c = "Hi\tGeeks"
print("\nTab: ")
print(c)

# Printing Paths with the
# use of New Line
d = "Nama:\nNRP:"
print("\npaths with new line: ")
print(d)

#3 Python String Formating (Example 1, 2, 3, 4)
#default order
print("\nEXAMPLE 1")
kal = "{} {} {}".format('Berliana', 'Sarlita', 'Rahajeng')
print("\nPrint string in default order")
print(kal)

kal = "{2} {1} {0}".format('Berliana', 'Sarlita', 'Rahajeng')
print("\nPrint string in positional order: ")
#Konten yang berbeda dari contoh di geekforgeek mendapat nilai tamban
print(kal)

kal = "{l} {j} {k}".format(j='Berliana', k='Sarlita', l='Rahajeng')
print ("\nPrint string in order of keywords: ")
print (kal)

print("\nEXAMPLE 2")
# Formatting of Integers
# Mengubah bilangan menjadi angka binernya
p = "{0:b}".format(7)
print("\nBinary representation of 7 is: ")
print(p)

# Formatting of Floats
#
q = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(q)

# Rounding off Integers
r = "{0:.2f}".format(22/7)
print("\nπ is: ")
print(r)

print("EXAMPLE 3")
# String alignment
Y = "|{:<15}|{:^15}|{:>15}|".format('Berliana','Sarlita','Rahajeng')
print("\nLeft, center and right alignment with Formatting: ")
print(Y)

# To demonstrate aligning of spaces
A = "\n{0:^25} will be a bachelor in {1:<3}!".format("Berliana",2028)
print(A)

print("\nEXAMPLE 4")
# Python Program for Old Style Formatting of Integers

Integer1 = 52.624652
print("\nFormatting in 3.3f format: ")
print('The value of Integer1 is %3.3f' % Integer1)
print("\nFormatting in 3.1f format: ")
print('The value of Integer1 is %3.1f' % Integer1)


"""
https://www.geeksforgeeks.org/python-string/
"""