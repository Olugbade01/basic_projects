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
        for each_item in file_list:

            
            each_item = dict(each_item)
            if not each_item.__contains__(delete_item):
                return "No such expense in here! Try again"
            else:
                for key in each_item.keys():
                    if key == delete_item:
                        file_list = file_list.__delattr__(each_item)
    return file_list

def cal_spending_by_category(file_list):

    file_list = list(file_list)
    amount_lists = []
    category_list = []
    for file in file_list:
        file = dict(file)
        amount_lists = []
        category_list = []
        for key, value in file.items():
            if key == "Category":
                category_list.append(value)
            if key == 'Amount':
                amount_lists.append(value)

    dict_categ_amount = dict(zip(category_list, amount_lists))

    return dict_categ_amount


