import json
import menu_operators
import utils

print('Welcome to your EXPENCE TRACKER')
# print("-" * 70)

name = input("What is your name?: ") 

file_name = utils.file_name_creator(name)

file_list = utils.create_read_file(file_name)
    
while True:

    menu = input(f"""
    ===========================================
    |                MENU LIST                |
    ===========================================
    What would you like to do?;
    (1) Add expense
    (2) View all expense
    (3) Calculate total spending
    (4) Calculate spending by category
    (5) Delete an expense
    (6) Save all expenses 
    (7) Exit
    ===========================================
    : """)
    print("    ===========================================")

    if utils.input_validator(menu):
        menu = int(menu)
        if menu == 1:

            expense = utils.add_expense()
            file_list.append(expense)
            print("-" * 70)
            print("Expense successfully added ")

            continue
        elif menu == 2:
            if len(file_list) == 0:
                print("Your expense list is empty")
            else:

                print("All Expenses!!!")
                print("-" * 120)
                print(file_list)
                print("-" * 120)

            continue

        elif menu == 3 :
            total_spending = menu_operators.total_spending_calculator(file_list)
            print(total_spending)
            continue
        elif menu == 4:
            if len(file_list) == 0:
                print("-" * 70)
                print("There is nothing here yet!! Spend some money.")
                print("-" * 70)
            else:
               
               by_category =  menu_operators.cal_spending_by_category(file_list)
            #    print("#######################################################################     Your Spending By Categories     ************************************************************")
               print("-" * 70)
               print('\n')
               print(by_category)
               print("-" * 70)

            #    print("************************************************************===================================================************************************************************")
            continue

        elif menu == 5:
            print("-" * 70)
            after_deletion = menu_operators.delete_expense(file_list)
            file_list = after_deletion

            continue

        elif menu == 6:

            utils.file_writer(file_name, file_list)
            print("-" * 70)
            print(f"All expense saved in {file_name} ")
            print("-" * 70)
        elif menu == 7:
            break

        else:
            print("-" * 70)
            print("Invalid option! Try again ")
    else:
        print("-" * 70)
        print("Enter a valid option 1 to 6!")
