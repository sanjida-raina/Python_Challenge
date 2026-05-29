usernames = ['rainangel','auvikbro', 'aknotok','char','admin']
for username in usernames:
    if username == 'admin':
        print('Hello admin. Would you like to see a status report?')
    else:
        print(f'Hello member, {username}.')

current_users = ['raina','auvik','pappa','mamma','rafoobah']
new_users = ['bob','john','mary','lily','rafoobah']
for usernames in new_users:
    if username == current_users:
        print('This username is already used. Enter a new username')
    
    else:
        if username in new_users:
            print('This username is available.')
#5.11
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        ordinal = "st"
    elif number == 2 :
        ordinal = "nd"
    elif number == 3:
        ordinal = "rd"
    else: ordinal = 'th'
    print(f'{number}{ordinal}')

