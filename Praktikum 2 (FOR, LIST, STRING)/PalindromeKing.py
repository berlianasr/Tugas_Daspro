S = input()  #string input dari pengguna
N = len(S)   #panjang string
pal = True   #asumsi bahwa string adalah palindrome

#loop untuk memeriksa apakah string adalah palindrome
for i in range(N // 2):  
    if S[i] != S[N - i - 1]:  #bandingkan karakter di depan dengan belakang
        pal = False
        break  #jika tidak sama, keluar dari loop

#output hasil
if pal:
    print("Palindrome King!")
else:
    print("Bukan King!")
