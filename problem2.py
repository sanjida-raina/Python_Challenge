#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
previous_num = 0


for value in range(0,10):
    current_value = value 
    sum = current_value + previous_num
    print(f" Current Number {current_value}  Previous Number {previous_num}  Sum: {sum}")
    previous_num = value
