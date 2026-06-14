
# Week 6 — Tuples and Final Python Fundamentals Review

## Problem 6: Coordinate Quadrant Finder

**Skill focus:** tuples, `if`/`elif`/`else`, coordinate pairs

A point on a graph can be written as a tuple: `(x, y)`.

Read `x` and `y` and print which quadrant the point is in.

If the point is on an axis or at the origin, print `AXIS`.

### Sample Input 1

```text
3 5
```

### Sample Output 1

```text
Quadrant 1
```

### Sample Input 2

```text
-2 4
```

### Sample Output 2

```text
Quadrant 2
```

### Sample Input 3

```text
0 7
```

### Sample Output 3

```text
AXIS
```

### Think Before Coding

- What does positive `x` and positive `y` mean?
- What if `x` is 0?
- Why is a coordinate pair like a tuple?

### Workspace / Notes

```text



```

---

## Problem 7: Sort Students by Score

**Skill focus:** list of tuples, sorting by second value

Each student has a name and a score.

Store each student as a tuple: `(name, score)`.

Print students from highest score to lowest score.

If scores tie, alphabetical order by name is okay.

### Sample Input 1

```text
4
Raina 92
Maya 85
Zara 99
Liam 92
```

### Sample Output 1

```text
Zara 99
Liam 92
Raina 92
Maya 85
```

### Sample Input 2

```text
3
Ava 70
Noah 88
Mia 88
```

### Sample Output 2

```text
Mia 88
Noah 88
Ava 70
```

### Think Before Coding

- Why is `(name, score)` a good tuple?
- How do we sort descending by score?
- What happens if two scores are equal?

### Workspace / Notes

```text



```

---

## Problem 8: Number and Cube Pairs

**Skill focus:** tuples, loops, list building

Read a list of numbers.

Create and print tuple pairs where each pair contains the number and its cube.

Example: `3` becomes `(3, 27)`.

### Sample Input 1

```text
4
1 2 3 4
```

### Sample Output 1

```text
1 1
2 8
3 27
4 64
```

### Sample Input 2

```text
3
5 0 -2
```

### Sample Output 2

```text
5 125
0 0
-2 -8
```

### Think Before Coding

- How do we calculate cube in Python?
- What information should each tuple store?
- Can a cube be negative?

### Workspace / Notes

```text



```

---

## Problem 9: Simple Gradebook with Functions

**Skill focus:** functions, dictionary, average, `if`/`else`

Write a program that reads student names and scores into a dictionary.

Then print the class average and the names of students who scored above or equal to the average.

Use at least one function in your solution.

### Sample Input 1

```text
4
Raina 90
Maya 80
Zara 100
Liam 70
```

### Sample Output 1

```text
Average: 85.0
Raina
Zara
```

### Sample Input 2

```text
3
Ali 60
Ben 60
Cara 90
```

### Sample Output 2

```text
Average: 70.0
Cara
```

### Think Before Coding

- What should the dictionary key be?
- How do we calculate average?
- Which students should be printed?

### Workspace / Notes

```text



```

---

## Problem 10: Final Mini Challenge — Contest Registration

**Skill focus:** mixed review: strings, lists, dictionaries, tuples, functions

A contest coach is registering students for teams.

Each line has a student name and a team name.

Print each team name and how many students are registered for that team.

Then print the team with the most students.

If there is a tie, any tied team is acceptable.

### Sample Input 1

```text
6
Raina Red
Maya Blue
Zara Red
Liam Red
Noah Blue
Ava Green
```

### Sample Output 1

```text
Blue 2
Green 1
Red 3
Largest Team: Red
```

### Sample Input 2

```text
5
A T1
B T2
C T1
D T2
E T3
```

### Sample Output 2

```text
T1 2
T2 2
T3 1
Largest Team: T1
```

### Think Before Coding

- What should the dictionary store?
- How do we update a team count?
- How do we find the largest count?

### Workspace / Notes

```text



```

---

# Final Reflection Before Moving to Java

## Which Python concept is strongest for me now?

```text

```

## Which concept still needs review?

```text

```

## Can I explain input, output, and plan before coding?

```text

```

## Can I solve a problem using a function?

```text

```

## What is one mistake I will avoid in Java?

```text

```

---

# Teacher Solution Sheet

> Keep this section separate from the student worksheet if printing for exam-style practice.

## Solution 1: Classroom Word Counter

```python
sentence = input().lower()
words = sentence.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word in sorted(counts):
    print(word, counts[word])
```

**Review note:** Dictionary counting pattern. `lower()` makes `Python` and `python` the same word.

---

## Solution 2: Unique Shopping Items

```python
n = int(input())
seen = set()
unique_items = []

for i in range(n):
    item = input()
    if item not in seen:
        seen.add(item)
        unique_items.append(item)

for item in unique_items:
    print(item)
```

**Review note:** Use a set for fast lookup and a list to preserve first-seen order.

---

## Solution 3: Password Basic Checker

```python
password = input()

has_upper = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_digit:
    print("VALID")
else:
    print("INVALID")
```

**Review note:** Boolean flags remember whether required character types were found.

---

## Solution 4: Student Score Summary

```python
n = int(input())
scores = list(map(int, input().split()))

highest = scores[0]
lowest = scores[0]
total = 0

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    total += score

average = total / n

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
```

**Review note:** Practice manual loop logic before using `sum()`, `max()`, and `min()`.

---

## Solution 5: First Repeated Word

```python
sentence = input().lower()
words = sentence.split()
seen = set()
answer = "NONE"

for word in words:
    if word in seen:
        answer = word
        break
    seen.add(word)

print(answer)
```

**Review note:** Because the first repeated word matters, stop as soon as it is found.

---

## Solution 6: Coordinate Quadrant Finder

```python
x, y = map(int, input().split())

point = (x, y)

if x == 0 or y == 0:
    print("AXIS")
elif x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
else:
    print("Quadrant 4")
```

**Review note:** The tuple `point` stores the coordinate pair, even though `x` and `y` are used for comparison.

---

## Solution 7: Sort Students by Score

```python
n = int(input())
students = []

for i in range(n):
    name, score_text = input().split()
    score = int(score_text)
    students.append((name, score))

students.sort(key=lambda item: (-item[1], item[0]))

for name, score in students:
    print(name, score)
```

**Review note:** Sort by negative score for descending score, then name for tie-breaking.

---

## Solution 8: Number and Cube Pairs

```python
n = int(input())
numbers = list(map(int, input().split()))

pairs = []
for num in numbers:
    pairs.append((num, num ** 3))

for num, cube in pairs:
    print(num, cube)
```

**Review note:** Tuples are good for fixed pairs like number and cube.

---

## Solution 9: Simple Gradebook with Functions

```python
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

n = int(input())
gradebook = {}

for i in range(n):
    name, score_text = input().split()
    gradebook[name] = int(score_text)

average = calculate_average(list(gradebook.values()))
print("Average:", average)

for name, score in gradebook.items():
    if score >= average:
        print(name)
```

**Review note:** Uses a function for average and a dictionary for name-score storage.

---

## Solution 10: Final Mini Challenge — Contest Registration

```python
n = int(input())
team_counts = {}

for i in range(n):
    student, team = input().split()
    team_counts[team] = team_counts.get(team, 0) + 1

for team in sorted(team_counts):
    print(team, team_counts[team])

largest_team = None
largest_count = -1
for team, count in team_counts.items():
    if count > largest_count:
        largest_count = count
        largest_team = team

print("Largest Team:", largest_team)
```

**Review note:** This is a mixed review problem: input, dictionary counting, sorting keys, and max tracking.

---

# Final Python Completion Checklist

- [ ] Reads input correctly using `input()`, `split()`, `map()`
- [ ] Uses `int()` and `float()` correctly
- [ ] Uses `if`/`elif`/`else` for decision logic
- [ ] Uses `for` and `while` loops when appropriate
- [ ] Uses lists for ordered data
- [ ] Uses dictionaries for counting and lookup
- [ ] Uses tuples for fixed pairs
- [ ] Writes and calls simple functions
- [ ] Tests with sample input/output
- [ ] Explains solution logic in plain English
