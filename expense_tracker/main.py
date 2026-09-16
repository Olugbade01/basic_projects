import json
print('Welcome to your EXPENCE TRACKER')

def input_validator(amount):
    try: 
        float(amount)
        return True

    except ValueError:
        return False

def add_expense():

    amount = input("Enter the amount of your expense: ")

    category = input('Enter the category of the expense: ')
    description = input('Describe the category of the the expense: ')

    if input_validator(amount):
        amount = amount

        result = {
            'Amount': amount,
            'Category': category,
            'Description': description
        }

    else:
        result = 'Enter a valid amount!'


    return result
report = []
name = input("What is your name?: ")
while True:

    menu = input("What would you like to do? (1) Add expense, (2) View account summary OR (3) Exit: ")

    if input_validator(menu):
        menu = int(menu)
        if menu == 1:

            expense = add_expense()
            report.append(expense)
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

with open(name + '.json', 'a') as file:
    json.dump(report, file)