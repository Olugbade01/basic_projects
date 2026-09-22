
import menu_operators
import utils

print('Welcome to your EXPENCE TRACKER')
print("-" * 70)

name = input("What is your name?: ").strip()
name = name.capitalize()

file_name = utils.file_name_creator(name)

file_list = utils.create_read_file(file_name)


while True:

    equal = "=" *50
    # print(equal)


    menu = input(f"""
    {equal}
                        MENU LIST                
    {equal}
    What would you like to do?;
    (1) Add expense
    (2) View all expense
    (3) Calculate total spending
    (4) Calculate spending by category
    (5) Delete an expense
    (6) Exit
    {equal}
    : """)
    print(f"    {equal}")

    if utils.input_validator(menu):
        menu = int(menu)
        if menu == 1:

            expense = utils.add_expense()
            file_list.append(expense)
            utils.file_writer(file_name, file_list)
            print("-" * 70)
            print("Expense successfully added ")


            continue
        elif menu == 2:
            if len(file_list) == 0:
                print("Your expense list is empty")
            else:

                print("All Expenses!!!")
                print("-" * 120)
                table = menu_operators.expense_viewer(file_list)
                print(table)
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
               print("-" * 70)
               print('\n      YOUR SPENDING BY CATEGORIES      \n')
               
               print(by_category)
               print("-" * 70)

            
            continue

        elif menu == 5:
            print("-" * 70)
            after_deletion = menu_operators.delete_expense(file_list)
            file_list = after_deletion
            utils.file_writer(file_name, file_list)

            continue

        elif menu == 6:

            print(f"Your expense's file is {file_name}")
            break

        else:
            print("-" * 70)
            print("Invalid option! Try again ")
    else:
        print("-" * 70)
        print("Enter a valid option 1 to 6!")
