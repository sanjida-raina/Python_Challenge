from datetime import datetime

import os
balance = 0
bonus = 50
balance += bonus
choice = 0
choice_history = [0]
statement= "Date \t\t Action \t Amount \t Balance"
date = "Dec 20th"

while choice != 9 :
    choice = int(input("What would you like to do?\n\t 1: Deposit \n\t 2: Withdraw \n\t 3: Check balance \n\t 4: Statement \n\t 9: Exit\n"))

    if choice == 1 :
        deposit = int(input("How much would you like to deposit?"))
        balance += deposit
        print("Here is your new balance:")
        print(balance)
        statement += (f"\n {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} \t Deposit \t {deposit} \t {balance}")
    elif choice == 2 :
        withdraw= int(input('How much would you like to withdraw?'))
        if balance <= withdraw:
            print("You can not withdraw more than you have")
        else:
            balance -= withdraw
        print(f"Here is your current balance:${balance}")
        statement += (f"\n{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} \t Withdraw \t {withdraw} \t {balance}")
    elif choice == 3:
        print(f"Here is your current balance:${balance}")
    elif choice == 4:
        print(statement)
    elif choice == 9:
        break
    else:
        print("Please enter a valid choice. \n")

    choice_history.append(choice)
    #_ = os.system('cls')
    print("\n =================== \n")

print(choice_history)







