musicians = ['emma','daniel','carl']
print(musicians)
counter = 0
for musician in musicians:
    print(musician.title())
    print (f"I am a musician. My name is {musician.title()}.")
    counter = counter + 1
    print(counter)
    
print('Thank you everyone for coming to the show!')