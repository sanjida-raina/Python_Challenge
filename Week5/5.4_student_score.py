numberScores = int(input())
listScores = input()
eachScores = listScores.split( )


for i in  range(len(eachScores)):
    eachScores[i] = int(eachScores[i])
    

highest = eachScores[0]
lowest = eachScores[0]
total = 0


for score in eachScores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    
    total = total + score


average = total/numberScores

print(f"Highest : {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")