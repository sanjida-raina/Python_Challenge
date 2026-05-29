n = int(input("start number: "))
x = int(input("end number: "))



for num in range(n,x+1):
    prime = True

    if num < 2:
        prime = False
    else:

        for i in range(2, num):
            if(num % i ==0):
                prime = False
            
    if prime==True:
        print(num)
            