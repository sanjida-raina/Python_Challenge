#armstrong number checker. the sum of each digit is raised to the power of the number of digits and checked with the original number.

num = int(input())
string_num = str(num)
digits = len(string_num)
total = 0

for i in string_num:
    number = int(i)
    total = total + (number**digits)

if total == num:
    print("YES")
else:
    print("NO")