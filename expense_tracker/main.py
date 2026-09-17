import json

import utils

print('Welcome to your EXPENCE TRACKER')


name = input("What is your name?: ") 

file_name = utils.file_name_creator(name)

if utils.file_name_checker(file_name):

    with open(file_name, "r") as file:
        file_list = json.load(file)

else:
    file_name = []

    with
while True:

    menu = input("What would you like to do? (1) Add expense, (2) View account summary OR (3) Exit: ")

    if utils.input_validator(menu):
        menu = int(menu)
        if menu == 1:

            expense = utils.add_expense()
            file_list.append(expense)
            print("Expense successfully added")
            continue
        elif menu == 2:
            print(f"Open {name}.json file in this directory")

            continue

        elif menu >= 3 :
            print("Enter a valid option 1, 2 or 3!")
            break
    else:
        print("Enter a valid option 1, 2 or 3!")

with open(file_name, 'a') as file:
    json.dump(file_list, file)