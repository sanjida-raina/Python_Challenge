word = "Metamorphase"

size = len(word)

print(f"Orginal String is  {word} this")

print("Orginal String is this", word , size) 


print("Printing only even index chars")
for c in range(0 , size-1):
    if c % 2 == 0:
        print(word[c])
