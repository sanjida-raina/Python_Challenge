for value in range(1,6):
    print(value)

myList = list(range(1,6))
print(myList)

for value in range(11,20):
    print(value*value)

myList2 = [1, 2, 3, 4, 5]

squaresList = []
cubeList = []
newList = []
for value in range(1,10):
    mySquare = value*value
    myCube = value*value*value
    squaresList.append(mySquare)
    cubeList.append(myCube)
    newList.append(myCube-mySquare)
    
print(cubeList)
print(squaresList)
print(newList)
print(min(cubeList))
print (max(cubeList))
print(sum(squaresList))
