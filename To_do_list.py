
#TODO: list comprehension improvement

todo_list = [] 
#add list to todo_list temporary variable so next time when program run it reads
#stored list

file = open('todos.txt', 'r')
todo_list_open = file.readlines() #update from the file
file.close()
   
for item in todo_list_open:
    item = item.replace("\n", "")
    todo_list.append(item)

box = "[ ] "

def print_numbered_list():
    for index, item in enumerate(todo_list, 1):
        item = item.replace("\n", "")
        print(f"({index})  {item}")

def print_list():
    file = open('todos.txt', 'r')
    todo_list = file.readlines() #update from the file
    file.close()
   
    for item in todo_list:
        item = item.replace("\n", "")
        print(item) 

while True:
    #TODO: add better formated menu
    #TODO: option to choose the list?
    user_choice = input("Type add, show, edit, complete or exit: ")
    
    if user_choice.startswith("add"):
        if user_choice[4:] != "":
            new_todo = user_choice[4:]
            new_todo = box + new_todo.upper()  #converts list into upper case
            todo_list.append(new_todo)  #update on the list
            
            file = open('todos.txt', 'w')  #update in the file
            for item in todo_list:
                file.writelines(f"{item}\n")
            file.close()
        elif user_choice[4:] == "":
            print("New Todo is not valid!")

    elif user_choice.startswith("show"):
        print_list()

    elif user_choice.startswith("edit"):
        if user_choice != "edit":
            print("Command is not valid! Type just 'edit'")
        
        else:
            print_numbered_list()

            #user choose which item
            choice_edit = input("Which item would you like to edit? Number: ")
            choice_edit = int(choice_edit) - 1
            replace_item = input(f"You are editing \"{todo_list[choice_edit]}\". New version: ")
            replace_item = replace_item.upper()
            todo_list[choice_edit] = todo_list[choice_edit][:4] + replace_item  #update on the list

            #clear the txt file
            with open("todos.txt",'w') as file:
                pass

            #write new todo_list again in the file
            file = open('todos.txt', 'w')  #update in the file
                        
            for item in todo_list:
                file.writelines(f"{item}\n")
            file.close()

            #print file
            print_list()

    elif user_choice.startswith("complete"):
        print_numbered_list()
        complete_choice = input("Which todo would you like to complete? Number: ")
        
        #check if user input is an integer
        is_integer = complete_choice.isnumeric()

#FIXME: What if user will input too big number?

        if is_integer == True:
            for index, item in enumerate(todo_list, 1):
                if index != int(complete_choice):
                    print(item)
                else:
                    item = item.replace("[ ] ", "[x] ")
                    complete_choice = int(complete_choice)
                    todo_list[complete_choice - 1] = item  #update on the list
            
            #clear the txt file
            with open("todos.txt",'w') as file:
                pass

            #write new todo_list again in the file
            file = open('todos.txt', 'w')  #update in the file
                        
            for item in todo_list:
                file.writelines(f"{item}\n")
            file.close()

            #print file
            print_list()

        else:
            print("Command not valid. Please type a number.")

#TODO: move completed task to the end?

    elif user_choice.startswith("exit"):
        cleanup_list = input("Would you like to clean up your list? yes/no: ")

        if cleanup_list == "yes":
            for item in todo_list:
                if "[x]" in item:
                    todo_list.remove(item)
        
        #clear the txt file
        with open("todos.txt",'w') as file:
            pass

        #write new todo_list again in the file
        file = open('todos.txt', 'w')  #update in the file
                    
        for item in todo_list:
            file.writelines(f"{item}\n")
        file.close()

        #print file
        print_list()

        break

    else:
        print("Command is not valid!")