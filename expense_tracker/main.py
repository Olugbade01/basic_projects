import json
print('Welcome to your EXPENCE TRACKER')


def amount_input_validator(amount):
    try: 
        float(amount)
        return True

    except ValueError:
        return False

def add_expense():

    amount = input("Enter the amount of your expense: ")

    category = input('Enter the category of the expense: ')
    description = input('Describe the category of the the expense: ')

    if amount_input_validator(amount):
        amount = amount

        result = {
            'Amount': amount,
            'Category': category,
            'Description': description
        }

    else:
        return ('Enter a valid amount!')


    return result

while True:

    menu = input("Want to add an expense? Y/N:")
    report = add_expense()

    with open("record.json", 'a') as file:
        json.dump(report, file)