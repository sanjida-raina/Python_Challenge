myList = input().lower().split( )
# print(myList)
indexEnd = len(myList)
found = False

for i in range(0, indexEnd):
    current = myList[i]
    for x in range(i+1, indexEnd):
        if current == myList[x]:
            found = True
            
    if found == True: 
        break
    

if found == True:
    print(current)
else:
    print("NONE")