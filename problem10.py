list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
resultlist = []
for value in list1 :
    if value % 2 == 1:
        resultlist.append(value)
        
for value in list2:
    if value % 2 ==0:
        resultlist.append(value)
print("result list:" , resultlist)