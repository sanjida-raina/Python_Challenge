from datetime import datetime

current_year = datetime.now().year


driver = input('What is your name?:')
DOB_year = input('Which year were you born?: ')
DOB_year = int(DOB_year)
age = current_year - DOB_year
if age < 16 :
    print(f'{driver.title()} is not allowed to drive.')

elif age < 18 :
    print(f'{driver.title()} can drive with supervision')

else:
    print(f'{driver.title()} can drive by yourself')