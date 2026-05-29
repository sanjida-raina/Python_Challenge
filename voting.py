name = input("What's your name?: ")
age =input('What is your age?:')
age = int(age)
if age >= 18 :
    print(f'{name} are old enough to vote')
else: 
    print(f'{name} is too young to vote')