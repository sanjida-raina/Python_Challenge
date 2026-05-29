# This will print the n-th Fibonacci number . 
# A Fibinacci number is sum of prevously 2 Fabinacci number , start with 0, 1

n = int(input())
first = 0
second = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else: 
    for i in range(2,n+1) :
        next_num = first + second
        first = second
        second = next_num

    print(second)