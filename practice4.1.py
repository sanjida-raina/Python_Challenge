input1 = input()
input2 = list(map(int, input().split(' ')))

print(input2)


total = 0
for i in input2:
    total = total + i

print(total)