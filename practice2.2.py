n = int(input("number: "))
prime = True

if (n < 2):
    prime = False

for i in range(2,n):
    if(n % i ==0):
        prime = False
        break

if prime == True :
    print("YES")
else:
    print("NO")