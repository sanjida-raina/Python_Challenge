# Raina Python Fundamentals Completion

## Final 2 Weeks Printable Worksheet — Before Moving to Java

**Goal:** Complete Python fundamentals review before transitioning to Java.

**Focus areas:**

- Strings
- Lists
- Dictionaries
- Tuples
- Functions
- Input/output
- Loop logic
- Simple contest-style problem solving

---

## Student Instructions

For each problem:

1. Read the problem carefully.
2. Identify the input and output.
3. Solve one sample by hand.
4. Write the Python code.
5. Test using the sample input/output.
6. Try one extra test case by yourself.
7. Explain your logic in one or two sentences.

---

# Week 5 — Strings, Lists, Dictionaries, and Functions

## Problem 1: Classroom Word Counter

**Skill focus:** strings, `split()`, dictionary counting, functions

Raina is helping a teacher count how many times each word appears in a sentence.

Write a function `count_words(sentence)` that returns a dictionary where each word is mapped to its frequency.

Treat uppercase and lowercase as the same. For this worksheet, assume there is no punctuation.

### Sample Input 1

```text
Python is fun and python is powerful
```

### Sample Output 1

```text
and 1
fun 1
is 2
powerful 1
python 2
```

### Sample Input 2

```text
Code code test
```

### Sample Output 2

```text
code 2
test 1
```

### Think Before Coding

- How can `lower()` help?
- Why is a dictionary useful?
- How do we sort dictionary keys?

### Workspace / Notes

```text



```

---

## Problem 2: Unique Shopping Items

**Skill focus:** lists, sets/dictionaries, order keeping

A shopping list may contain duplicate items.

Print each unique item only once, in the order it first appeared.

### Sample Input 1

```text
6
apple
banana
apple
milk
banana
rice
```

### Sample Output 1

```text
apple
banana
milk
rice
```

### Sample Input 2

```text
5
pen
pen
pencil
eraser
pen
```

### Sample Output 2

```text
pen
pencil
eraser
```

### Think Before Coding

- Why should order be preserved?
- Can a set alone remember order clearly?
- What does “first appeared” mean?

### Workspace / Notes

```text



```

---

## Problem 3: Password Basic Checker

**Skill focus:** strings, boolean flags, `if`/`else`

A website wants a simple password checker.

A password is **VALID** if it has:

- at least 8 characters,
- at least one uppercase letter,
- at least one digit.

Print `VALID` or `INVALID`.

### Sample Input 1

```text
Raina2026
```

### Sample Output 1

```text
VALID
```

### Sample Input 2

```text
pythonclass
```

### Sample Output 2

```text
INVALID
```

### Think Before Coding

- How do we check each character?
- What boolean variables do we need?
- What is the final condition?

### Workspace / Notes

```text



```

---

## Problem 4: Student Score Summary

**Skill focus:** lists, loops, max/min/average, function design

Write a program that reads student scores and prints:

- highest score,
- lowest score,
- average score.

Do **not** use built-in `max()`, `min()`, or `sum()` for the main solution. Practice loop thinking.

### Sample Input 1

```text
5
80 92 75 88 95
```

### Sample Output 1

```text
Highest: 95
Lowest: 75
Average: 86.0
```

### Sample Input 2

```text
4
100 90 80 70
```

### Sample Output 2

```text
Highest: 100
Lowest: 70
Average: 85.0
```

### Think Before Coding

- What starting value should highest and lowest have?
- How do we update total?
- Why is average `total / N`?

### Workspace / Notes

```text



```

---

## Problem 5: First Repeated Word

**Skill focus:** strings, dictionary/set lookup, early stopping

Given a sentence, print the first word that appears for the second time.

Treat uppercase and lowercase as the same. If no word repeats, print `NONE`.

### Sample Input 1

```text
I like Python because Python is fun
```

### Sample Output 1

```text
python
```

### Sample Input 2

```text
red blue green yellow
```

### Sample Output 2

```text
NONE
```

### Think Before Coding

- Why does order matter?
- What should happen when a repeated word is found?
- Should the loop continue after finding it?

### Workspace / Notes

```text



```

---
