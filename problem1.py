#Given two integer numbers, write a Python program to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.

def myFunction (number1, number2):
    product = number1 * number2
    if product > 1000:
        return number1 + number2
    else:
        return product



myNumber1 = int(input('Number 1 = '))
myNumber2 = int(input('Number 2 = '))


result = myFunction(myNumber1 , myNumber2)


print(f'The result is {result}')

