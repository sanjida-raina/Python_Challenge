# This will check if a provided number is Fabonacci

n = int(input())

first = 0
second = 1
find = False

if n == 0 or n == 1:
    find = True
else:
    while (n > second) :
        next_num = first + second
        if n == next_num:
            find = True

        first = second
        second = next_num

if find == True:
    print("YES")
else:
    print('NO')


