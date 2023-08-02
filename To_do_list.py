

todo_list = [] 
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
    choice_1 = input("Type add, show, edit, complete or exit: ")
    
    match choice_1:
        case "add":
            new_todo = input("Enter a todo: ")
            new_todo = box + new_todo.upper()  #converts list into upper case
            todo_list.append(new_todo)  #update on the list
            
            file = open('todos.txt', 'w')  #update in the file
            for item in todo_list:
                file.writelines(f"{item}\n")
            file.close()

        case "show":
            print_list()

        case "edit":
            print_numbered_list()

            #do this to todo_list
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
#FIXME: 
#TODO: Make it working with file!
        case "complete":
            print_numbered_list()
            complete_choice = input("Which todo would you like to complete? Number: ")
            
            for index, item in enumerate(todo_list, 1):
                if index != int(complete_choice):
                    print(item)
                else:
                    item = item.replace("[ ] ", "[x] ")
                    complete_choice = int(complete_choice)
                    todo_list[complete_choice - 1] = item  #update on the list
                    print(item)

#TODO: move completed task to the end?
#TODO: Make it working with file!

        case "exit":
            cleanup_list = input("Would you like to clean up your list? yes/no: ")

            if cleanup_list == "yes":
                for item in todo_list:
                    if "[x]" in item:
                        todo_list.remove(item)
            
            for item in todo_list:
                print(item)

            break




