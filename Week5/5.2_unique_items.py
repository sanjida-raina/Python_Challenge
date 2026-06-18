input = input()
shoppingList = input.split( )

unique = dict.fromkeys(shoppingList)
uniqueList = list(dict.fromkeys(shoppingList))

print(uniqueList)