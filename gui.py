from modules.functions import reset_txt_list, print_list, print_numbered_list, print_menu 
from modules.global_variables import todo_list, box
import PySimpleGUI as sg

sg.theme("BrightColors")
input_box_label = sg.Text("Type in a todo")

input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")
todo_add_button = sg.Button("add")

filepath_input_box_label = sg.Text("Type in a name of your list")
filepath_input_box = sg.InputText(tooltip="Enter the name of your todo list",
                                  key="filepath")
filepath_open_button = sg.Button("open")

window = sg.Window('My ToDo App',
                   layout=[[input_box_label],
                           [input_box, todo_add_button]], 
                   font=("Lato", 16))

# [filepath_input_box_label],
# [filepath_input_box, filepath_open_button],

while True:
    user_choice, values = window.read()
    # filepath = filepath + ".txt"
    # print(filepath)
    filepath = "todos.txt"
    print(user_choice)
    print(values)

    if user_choice.startswith("add"):
        reset_txt_list(filepath, todo_list)
        values = values["todo"]
        if values != "":
            new_todo = values
            new_todo = box + values.upper()  #converts list into upper case
            todo_list.insert(0, values)  #insert on the top of the list
            
            reset_txt_list(filepath, todo_list)  #update in the file
        
    #     elif user_choice[4:] == "":
    #         print("New Todo is not valid!")

    # elif user_choice.startswith("show"):
    #     print_list(filepath)

    # elif user_choice.startswith("edit"):
    #     reset_txt_list(filepath, todo_list)

    #     if user_choice != "edit":
    #         print("Command is not valid! Type just 'edit'")
        
    #     else:
    #         print_numbered_list(filepath)

    #         #user choose which item
    #         choice_edit = input("Which item would you like to edit? Number: ")

    #         #check if user input is an integer
    #         edit_is_integer = choice_edit.isnumeric()
    #         #count = 0

    #         if edit_is_integer == True:
    #             #number of lines in the file
    #             with open (filepath, "r") as file:
    #                 for count, line in enumerate(file):
    #                     pass

    #             choice_edit = int(choice_edit) - 1

    #             if choice_edit >= 0 and choice_edit <= count:
    #                 replace_item = input(f"You are editing \"{todo_list[choice_edit]}\". New version: ")
    #                 replace_item = replace_item.upper()
    #                 todo_list[choice_edit] = todo_list[choice_edit][:4] + replace_item  #update on the list

    #                 reset_txt_list(filepath, todo_list)

    #                 #print file
    #                 print_list(filepath)

    #             else:  #else if user input number is not correct, less than 1 or more than tosos available
    #                 print(f"Number is not correct. Type any number between 1 and {count + 1}.")

    #         else:  #else if user input is not number
    #             print("Command not valid. Please type a number.")




window.close()