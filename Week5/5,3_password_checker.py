password = input()

upper = False
digit = False

if len(password) >= 8:
    length = True
else:
    length = False

for i in password:
    if i.isupper():
        upper = True
    if i.isdigit():
        digit = True

if upper == True and digit == True and length == True :
    print("VALID")
else:
    print("INVALID")