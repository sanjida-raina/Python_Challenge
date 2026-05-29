def same_num (numbers):
    first_number = numbers[0]
    last_number = numbers[-1]

    if first_number == last_number:
        return True
    else:
        return False




# testing 

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

# calling the Funtions 
r1 = same_num(numbers_x)

r2 = same_num(numbers_y)
 ## printing the result 
print(r1)
print(r2)

print(same_num([75, 65, 35, 75, 30]))
