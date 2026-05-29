# Given Input: a = 5, b = 10

# Expected Output:

# Before Swap: a = 5, b = 10
# After Swap: a = 10, b = 5

a = 5
b= 10

print("Before Swap: a =",a, " b = ", b)
a,b = b,a
print("After Swap: a =",a, " b = ", b)