import json


def file_name_checker(file_name):
    try:
        with open(file_name, "r") as file:
            json.load(file)
        
        return True
    except OSError:
    
        return False
        
def input_validator(value):
    try: 
        int(value)
        return True

    except ValueError:
        return False

def get_valid_float(prompt):

   try:
       float(prompt)
       return True
   except ValueError:
       return False

def add_expense():


    while True:

        stramount = input("Enter the amount of the expense you want to add: ").strip()

        if get_valid_float(stramount):
            amount = float(stramount) 
            if amount > 0:
                amount = amount
            
                break
            else:
                print("Amount can't be less than or equal to 0")
        else:
            print("Enter a valid number, Try again!!!")

    while True:


        category = input("Enter the category of the expense(Food, Transportation, Utility,...): ").title().strip()
        if category != "":
            category = category
            break
        else:
            print("Category cannot be empty")
    while True:

        description = input("Describe the category of the expense(Lunch, Gift from brother,...): ").strip()

        if description != "":
            description = description
            break
        else:
            print('Description cannot be empty')

    result = {
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    
    
    return result


    
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