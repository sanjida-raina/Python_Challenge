n = int(input())
students= []

for i in range(n):
    name, scoreText = input().split()
    score = int(scoreText)
    students.append((name,score))

# students = students.sorted()
# print(students)

for name, score in students:
    print(f"{name} => {score}")

