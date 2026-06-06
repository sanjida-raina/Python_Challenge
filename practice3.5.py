number = int(input())
str_num = str(number)
total = 0

for i in str_num:
    num = int(i)
    total = total + num

print(total)
