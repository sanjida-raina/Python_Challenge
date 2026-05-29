n = int(input("Put a number: "))
total = 1

if n == 0 or n==1:
    print(1)


else: 
    for i in range(1,n+1):
        total = total * i

    print(total)