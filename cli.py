
from modules.functions import print_menu, read_todo_list, print_numbered_list, print_list, reset_txt_list
from modules.global_variables import todo_list, box

#welcome message and menu    
print("Welcome in todo list program!")

while True:
    try: 
        filepath = input("Which list you would like to work on?\nType in the name of the list.\nIf you would like to create a new list, type 'new list' <name>: ")
        filepath = filepath + ".txt"
        if filepath.startswith("new list"):
            todo_list = []  #earease todolist
            new_list = filepath[8:]
            print(f"Your new list is called: \"{new_list}\".")
            with open(new_list, 'w') as new_todo_list:   
                new_todo_list.write   #create new file

            filepath = new_list
            user_file = open(filepath, 'r')
            user_file.close()
            print(f"You are working on \"{filepath}\" list.")

            read_todo_list(filepath)
            print_list(filepath)
            break

        else:    
            user_file = open(filepath, 'r')
            user_file.close()
            break
            
    except OSError as error_message:
        print(f"\nThis file does not exist: {error_message}! Please try again!")  

print_menu()
read_todo_list(filepath)   
print_list(filepath)


while True:
    user_choice = input("Type the command: ")
    
    if user_choice.startswith("add"):
        reset_txt_list(filepath, todo_list)
        if user_choice[4:] != "":
            new_todo = user_choice[4:]
            new_todo = box + new_todo.upper()  #converts list into upper case
            todo_list.insert(0, new_todo)  #insert on the top of the list
            
            reset_txt_list(filepath, todo_list)  #update in the file
        
        elif user_choice[4:] == "":
            print("New Todo is not valid!")

    elif user_choice.startswith("show"):
        print_list(filepath)

    elif user_choice.startswith("edit"):
        reset_txt_list(filepath, todo_list)

        if user_choice != "edit":
            print("Command is not valid! Type just 'edit'")
        
        else:
            print_numbered_list(filepath)

            #user choose which item
            choice_edit = input("Which item would you like to edit? Number: ")

            #check if user input is an integer
            edit_is_integer = choice_edit.isnumeric()
            count = 0

            if edit_is_integer == True:
                #number of lines in the file
                with open (filepath, "r") as file:
                    for count, line in enumerate(file):
                        pass

                choice_edit = int(choice_edit) - 1

                if choice_edit >= 0 and choice_edit <= count:
                    replace_item = input(f"You are editing \"{todo_list[choice_edit]}\". New version: ")
                    replace_item = replace_item.upper()
                    todo_list[choice_edit] = todo_list[choice_edit][:4] + replace_item  #update on the list

                    reset_txt_list(filepath, todo_list)

                    #print file
                    print_list(filepath)

                else:  #else if user input number is not correct, less than 1 or more than tosos available
                    print(f"Number is not correct. Type any number between 1 and {count + 1}.")

            else:  #else if user input is not number
                print("Command not valid. Please type a number.")


    elif user_choice.startswith("tick"):
        print_numbered_list(filepath)
        complete_choice = input("Which todo would you like to tick? Number: ")
        
        #check if user input is an integer
        complete_is_integer = complete_choice.isnumeric()
        count = 0  #reset count variable after other commands like edit

        if complete_is_integer == True:
            #number of lines in the file
            with open (filepath, "r") as file:
                for count, line in enumerate(file):
                    pass

            complete_choice = int(complete_choice) #change to int before comparsion operator 
            

            if complete_choice > 0 and complete_choice <= count + 1:
                for index, item in enumerate(todo_list, 1):
                    if index != int(complete_choice):
                        pass
                    else:
                        item = item.replace("[ ] ", "[x] ")
                        complete_choice = int(complete_choice)
                        todo_list[complete_choice - 1] = item  #update on the list

                        # attach ticked tasks at the end
                        
                        complete_list = []
                        for item in todo_list:
                            if "[x]" in item:
                                complete_list.append(item)
                                todo_list.remove(item)

                        for item in complete_list:
                            todo_list.append(item)

                reset_txt_list(filepath, todo_list)

                #print file
                print_list(filepath)

            else:  #else if user input number is not correct, less than 1 or more than tosos available
                print(f"Number is not correct. Type any number between 1 and {count + 1}.")

        else:  #else if user input is not number
            print("Command not valid. Please type a number.")

    elif user_choice.startswith("cleanup"):
        clean_list = []
        for item in todo_list:
            if item.startswith("[x]"):
                pass
            else:
                clean_list.append(item)
                #replace todo_list with clean_list to file
        
        todo_list = clean_list
        reset_txt_list(filepath, todo_list)
    
        #print file
        print_list(filepath)

    elif user_choice.startswith("menu"):
        print_menu()

    elif user_choice.startswith("switch"):
        if user_choice[7:] != "":
            while True:
                try: 
                    filepath = user_choice[7:] + ".txt"
                    user_file = open(filepath, 'r')
                    user_file.close()
                    print(f"You are working on \"{filepath}\" list.")
                    #update todo_list variable
                    with open(filepath, 'r') as file:
                        todo_list_replace = file.readlines()  #update from the file
                    todo_list = []   #clean variable
                    #  write again from new txt file
                    for item in todo_list_replace:
                        item = item.replace("\n", "")
                        todo_list.append(item)
                    
                    #clear the screen
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_menu()
                    print_list(filepath)
                    break
                        
                except OSError as error_message:
                    print(f"\nThis file does not exist: {error_message}! Please try again!")
                    break
    
    elif user_choice.startswith("new list"):
        if user_choice[8:] != "":
            todo_list = []  #earease todolist
            new_list = user_choice[9:]
            print(f"Your new list is called: \"{new_list}\".")
            new_list = str(new_list) + ".txt"
            with open(new_list, 'w') as new_todo_list:   
                new_todo_list.write   #create new file

            filepath = new_list
            user_file = open(filepath, 'r')
            user_file.close()
            print(f"You are working on \"{filepath}\" list.")

            read_todo_list(filepath)
            print_list(filepath)

        else:
            print("Please add your new list name!")


    elif user_choice.startswith("exit"):
        break
    
    else:
        print("Command is not valid!")