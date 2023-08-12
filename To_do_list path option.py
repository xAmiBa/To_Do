
#TODO: list comprehension improvement
#import os   #operating system dependent functionality. Interaction with file path.

todo_list = []  #stored list
box = "[ ] "

#welcome message and menu    
print("Welcome in todo list program!")

while True:
    try: 
        filepath = input("Which list you would like to work on? Type in the name of the file: ")
        user_file = open(filepath, 'r')
        user_file.close()
        break
            
    except OSError as error_message:
        print(f"\nThis file does not exist: {error_message}! Please try again!")

print("\nMenu:\n* add <your todo>\n* show\n* edit\n* complete\n* menu\n* exit\n")

#filepath = "todos.txt"

#Function: read todo list from txt file and formats it removing empty lines
def read_todo_list(filepath):
    with open(filepath, 'r') as file:
        todo_list_open = file.readlines()  #update from the file

    for item in todo_list_open:
        item = item.replace("\n", "")
        todo_list.append(item)

    file.close()  

#Function: list from variable 
def write_todo_list(filepath):
    file = open(filepath, 'w')  #update in the file
    for item in todo_list:
        file.writelines(f"{item}\n")
    file.close()


read_todo_list(filepath)   

#  Function prints 
def print_numbered_list():
    for index, item in enumerate(todo_list, 1):
        item = item.replace("\n", "")
        print(f"({index})  {item}")
    print("")

def print_list(filepath):
    file = open(filepath, 'r')
    todo_list = file.readlines() #update from the file
    file.close()

    print("\nMY TODO LIST:")
    for item in todo_list:
        item = item.replace("\n", "")
        print(item) 
    print("")

def reset_txt_list(filepath):
    #clear the txt file
    with open(filepath,'w') as file:
        pass
    #write new todo_list again in the file
    write_todo_list(filepath)  #update in the file    


while True:
    #TODO: option to choose the list? next lesson
    user_choice = input("Type the command: ")
    
    if user_choice.startswith("add"):
        if user_choice[4:] != "":
            new_todo = user_choice[4:]
            new_todo = box + new_todo.upper()  #converts list into upper case
            todo_list.append(new_todo)  #update on the list
            
            reset_txt_list(filepath)  #update in the file
        
        elif user_choice[4:] == "":
            print("New Todo is not valid!")

    elif user_choice.startswith("show"):
        print_list(filepath)

    elif user_choice.startswith("edit"):
        if user_choice != "edit":
            print("Command is not valid! Type just 'edit'")
        
        else:
            print_numbered_list()

            #user choose which item
            choice_edit = input("Which item would you like to edit? Number: ")

            #check if user input is an integer
            edit_is_integer = choice_edit.isnumeric()
            #count = 0

            if edit_is_integer == True:
                #number of lines in the file
                with open ("todos.txt", "r") as file:
                    for count, line in enumerate(file):
                        pass

                choice_edit = int(choice_edit) - 1

                if choice_edit >= 0 and choice_edit <= count:
                    replace_item = input(f"You are editing \"{todo_list[choice_edit]}\". New version: ")
                    replace_item = replace_item.upper()
                    todo_list[choice_edit] = todo_list[choice_edit][:4] + replace_item  #update on the list

                    reset_txt_list(filepath)

                    #print file
                    print_list(filepath)

                else:  #else if user input number is not correct, less than 1 or more than tosos available
                    print(f"Number is not correct. Type any number between 1 and {count + 1}.")

            else:  #else if user input is not number
                print("Command not valid. Please type a number.")


    elif user_choice.startswith("complete"):
        print_numbered_list()
        complete_choice = input("Which todo would you like to complete? Number: ")
        
        #check if user input is an integer
        complete_is_integer = complete_choice.isnumeric()
        count = 0  #reset count variable after other commands like edit

        if complete_is_integer == True:
            #number of lines in the file
            with open ("todos.txt", "r") as file:
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
                
                reset_txt_list(filepath)

                #print file
                print_list(filepath)

            else:  #else if user input number is not correct, less than 1 or more than tosos available
                print(f"Number is not correct. Type any number between 1 and {count + 1}.")

        else:  #else if user input is not number
            print("Command not valid. Please type a number.")

#TODO: move completed task to the end?

    elif user_choice.startswith("exit"):
        cleanup_list = input("Would you like to clean up your list? y/n: ")

        if cleanup_list == "y":
            for item in todo_list:
                if "[x]" in item:
                    todo_list.remove(item)
        
        reset_txt_list(filepath)

        #print file
        print_list(filepath)

        break

    elif user_choice.startswith("menu"):
        print("\nMenu:\n* add <your todo>\n* show\n* edit\n* complete\n* menu\n* exit\n")

    else:
        print("Command is not valid!")