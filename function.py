#from myLIB import pet

def greet_user(username):
    print(f"Hello {username.title()}")

greet_user('jesse')


    
#pet.describe_pet('cat','tushi')

def get_formatted_name(first_name,last_name):
    full_name= f"{first_name} {last_name}"
    return full_name.title()

musician= get_formatted_name('jimmy', 'hobbledorn')
print(musician)