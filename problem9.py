original_num = input("input a number: ")
num = list(original_num)
k = int(len(num)/2)
print(f"original number {original_num}")
result = True
for i in range(k):
    ci = -(i+1)
    if num[i] != num[ci]:
        result = False
        break

if result == False:
    print("No. given number is not palindrome number")
else:
    print("Yes. given number is palindrome number")