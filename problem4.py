def remove_chars(word, n):
    # write your code
    print('Original string: ', word)
    new_word = word[n:]
    return new_word

print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'