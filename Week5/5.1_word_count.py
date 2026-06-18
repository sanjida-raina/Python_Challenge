# sentence = input()
sentence = "I am dancing i am on the moon"
words = sentence.split( )
# words = words.sort()
print(words)

counter = {}

for word in words:
    counter[word] = counter.get(word,0) + 1


print(counter)

