import json
import menu_operators
import utils

print('Welcome to your EXPENCE TRACKER')


name = input("What is your name?: ") 

file_name = utils.file_name_creator(name)

file_list = utils.create_read_file(file_name)
    
while True:

    menu = input(f"""What would you like to do? 
    (1) Add expense
    (2) View all expense
    (3) Calculate total spending
    (4) Calculate spending by category
    (5) Delete an expense
    (6) Save all expenses: """)

    if utils.input_validator(menu):
        menu = int(menu)
        if menu == 1:

            expense = utils.add_expense()
            file_list.append(expense)
            print("Expense successfully added")
            continue
        elif menu == 2:
            if len(file_list) == 0:
                print("Your expense list is empty")
            print(file_list)

            continue

        elif menu == 3 :
            total_spending = menu_operators.total_spending_calculator(file_list)
            print(total_spending)
            continue
        elif menu == 4:
            if len(file_list) == 0:
                print("There is nothing here yet!! Spend some money.")
            else:
               res =  menu_operators.cal_spending_by_category(file_list)
               print(res)
            continue

        elif menu == 5:
            after_deletion = menu_operators.delete_expense(file_list)
            file_list = after_deletion
            print("Expense successfully deleted.")
            continue

        elif menu == 6:

            utils.file_writer(file_name, file_list)

        else:
            print("Invalid option! Try again ")
    else:
        print("Enter a valid option 1 to 6!")
