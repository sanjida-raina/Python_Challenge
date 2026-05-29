principal_amnt = int(input())
rate = int(input())
time = int(input())

amount = principal_amnt * (1 + rate/100)**time
compound = amount - principal_amnt
print(compound)
