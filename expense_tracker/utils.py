import json


def file_name_checker(file_name):
    try:
        with open(file_name, "r") as file:
            json.load(file)
        
        return True
    except OSError:
    
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
        return 'Enter a valid amount!'


    return result
def input_validator(amount):
    try: 
        float(amount)
        return True

    except ValueError:
        return False

def file_name_creator(name):
    file_Name = ""
    name = str(name).strip()
    if name.endswith('.json'):

        file_Name = name 

    elif not name.endswith(".json") and name.isidentifier():

        file_Name = name + ".json"

    else:

        file_Name = "Error!  Enter a valid variable name"

    return file_Name

def create_read_file(file_name):

    if file_name_checker(file_name):

        with open(file_name, "r") as file:
            file_list = json.load(file)

    else:
        file_content  = []

        file_writer(file_name, file_content)

        with open(file_name, "r") as f:
            file_list = json.load(f)

    return file_list

def file_writer(file_Name, file_Content):

    with open(file_Name, "w") as file:
        file_written = json.dump(file_Content, file, indent=4)

    return file_written