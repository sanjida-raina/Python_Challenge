zoo_animals = ['tiger', 'elephant','turtle','monkey','lion','zebra' ]
search_animal = input('What animal are you looking for at the zoo?')
search_animal = search_animal.lower() #making user input as lowercase
search_animal = search_animal.strip() #taking out whitespace at the start and end
if search_animal in zoo_animals:
    print(f'{search_animal.title()} is at the zoo. Enjoy your day!')

else:
    print(f'Sorry we do not have {search_animal} at our zoo') 