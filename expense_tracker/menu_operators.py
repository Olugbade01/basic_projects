import utils


def total_spending_calculator(listed_dict):
    report = ""
    file_list = list(listed_dict)
    if len(file_list) == 0:
        report = "You have no record here!"
    
    else:
        total = 0
        for  each_expense in file_list:
            for key, value in each_expense.items():
    
                if key == "Amount":
                     total += value
        report = f"Your total expense is {total}"
    return report

def delete_expense(listed_dicts):
    file_list = list(listed_dicts)
    if len(file_list) == 0:

        print("There is nothing to delete here!")

    else:
        while True:

            index_del = input(expense_viewer(file_list)+"\nChoose the S/N of the item you want to delete: ")
            
            if utils.input_validator(index_del):
                index_del = int(index_del)
                i = 0
                while i < len(file_list):
                    i += 1
                    if index_del == i:
                        file_list.remove(file_list[i-1])
                        print("""===========================================
Expense successfully deleted.
===========================================""")
                        break
                else:
                    print(f"Enter a valid option 1 to {len(file_list)} ")
                break
            else:
                print(f"Enter a valid option 1 to {len(file_list)} ")


    return file_list

def cal_spending_by_category(file_list):
    spending_by_cat = {}

    for file in file_list:
        if file['Category'] in spending_by_cat:
            spending_by_cat[file['Category']] += file['Amount']

        else:
             spending_by_cat[file['Category']] = file['Amount']

    lst_cate_totals = []
    for key, value in spending_by_cat.items():
        result = {
            "Amount": value,
            "Category": key
        }
        lst_cate_totals.append(result)

    table_cat = f'{"S/N":<5}  {'Category':<15}{'Amount':>12}\n'
    for i, each_dict in enumerate(lst_cate_totals):
            table_cat +=f'{i+1:<5}  {each_dict['Category']:<15}{each_dict["Amount"]:>12}\n'
    return table_cat



def expense_viewer(list_file):
    table = f'{"S/N":<5}  {'Category':<15}{'Amount':>12}   Description\n'
    for i, each_dict in enumerate(list_file):
        table +=f'{i+1:<5}  {each_dict['Category']:<15}{each_dict["Amount"]:>12}   {each_dict['Description']}\n'

    return table