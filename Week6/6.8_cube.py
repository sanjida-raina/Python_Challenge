totalNumbers = int(input())
numberStrings = input().split()

for i in numberStrings:
    num = int(i)
    cube = num**3

    print(num, cube)
