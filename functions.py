from global_variables import todo_list

#Function: print menu
def print_menu():
    print("\nMenu:\n* add <your todo>\n* show\n* edit\n* complete\n* menu\n* switch <list name>\n* tick\n* exit\n")

#Function: read todo list from txt file and formats it removing empty lines
def read_todo_list(filepath):
    with open(filepath, 'r') as file:
        todo_list_open = file.readlines()  #update from the file

    for item in todo_list_open:
        item = item.replace("\n", "")
        todo_list.append(item)

    file.close()  

#  Function prints 
def print_numbered_list(filepath):
    file = open(filepath, 'r')
    todo_list = file.readlines() #update from the file
    
    for index, item in enumerate(todo_list, 1):
        item = item.replace("\n", "")
        print(f"({index})  {item}")
    file.close()
    print("\n")

def print_list(filepath):
    file = open(filepath, 'r')
    todo_list = file.readlines() #update from the file
    file.close()

    print("\nMY TODO LIST:")
    for item in todo_list:
        item = item.replace("\n", "")
        print(item) 
    print("")

def reset_txt_list(filepath, source):
    #clear the txt file
    with open(filepath,'w') as file:
        pass
    #write new todo_list again in the file
    file = open(filepath, 'w')  #update in the file
    for item in source:
        file.writelines(f"{item}\n")
    file.close()  #update in the file    