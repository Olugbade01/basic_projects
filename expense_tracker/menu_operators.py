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

        delete_item = input("Enter the category of the item you would like to delete: ")
        delete_item = delete_item.strip()
        i = 0
        while i < len(file_list):
            try:
                i += 1
                if listed_dicts[i]["Category"] == delete_item:
                    file_list.remove(file_list[i])
                    print("""===========================================
Expense successfully deleted.
===========================================""")
                    break
                else:
                    continue
            except IndexError:
                print('No such file here!')


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
    return lst_cate_totals



