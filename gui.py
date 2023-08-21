from modules.functions import reset_txt_list, print_list, print_numbered_list, print_menu, read_todo_list
from modules.global_variables import todo_list, box
import PySimpleGUI as sg

sg.theme("BrightColors")
sg.set_options(font=("Lato", 14))
filepath = "todos.txt"
read_todo_list(filepath) 

# NEW TO DO FUNCTIONALITY
input_box_label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")
todo_add_button = sg.Button("add")

# EDIT FUNCTIONALITY
edit_listbox = sg.Listbox(values=todo_list,
                          key="edit_todos",
                          enable_events=True,
                          size=[45, 10])
edit_button = sg.Button("edit")

#  TICK FUNCTIONALITY
tick_button = sg.Button("\u2713", key="tick")

#  CLEANUP FUNCTIONALITY
cleanup_button = sg.Button("cleanup", key="clean_list")

# SWITCH FILEPATH
switch_box_label = sg.Text("Type in list name. If new list, type \"new\":")

switch_box = sg.InputText(tooltip="Entera new file name",
                          key="new_file")
switch_button1 = sg.Button("switch list", key="switch_button")
switch_button2 = sg.Button("switch", key = "switch_final")

# A TO DO LIST VIEW 
todo_list_view = sg.Listbox(values=todo_list,
                            size=(20, len(todo_list)),
                            key="list_view",
                            enable_events=True,
                            )

# MAIN WINDOW
column1 = [[todo_list_view]]
column2 = [
    [input_box_label],
    [input_box],
    [todo_add_button, edit_button, tick_button, cleanup_button]
    ]

layout = [[sg.Column(column1), sg.Column(column2)]]

window = sg.Window('My ToDo App', layout)

# switch_window = sg.Window("switch ToDo list",
#                           [[switch_box_label],
#                            [switch_box],
#                            [switch_button2]])

while True:
    user_choice, values = window.read()

    print(user_choice) #button value / key
    print(values) #all values off all buttons/keys
    
    if user_choice == "add":
        reset_txt_list(filepath, todo_list)
        
        if values["todo"] != "":
            new_todo = values["todo"]
            new_todo = box + new_todo.capitalize()  #converts list into upper case
            todo_list.insert(0, new_todo)  #insert on the top of the list
            reset_txt_list(filepath, todo_list)  #update in the file
            window["list_view"].update(todo_list)

        elif values["todo"] == "":
            pass 

    if user_choice == "edit":
        if values["todo"] != "":
            reset_txt_list(filepath, todo_list)        

            choice_edit = values["list_view"][0] #we point to "edit" key for the corresponding value and number of choice

            new_edit = values["todo"] #user will write new todo in input widow belonging to todo key

            index = todo_list.index(choice_edit)
            todo_list[index] = todo_list[index][:4] + new_edit #only stuff after the box

            with open (filepath, "r") as file:
                for count, line in enumerate(file):
                    pass

            reset_txt_list(filepath, todo_list)
            window["list_view"].update(todo_list)

        elif values["todo"] == "":
            pass 

    elif user_choice == "tick":
        if values["list_view"] != "":
            reset_txt_list(filepath, todo_list)        

            choice_tick = values["list_view"][0] #we point to "edit" key for the corresponding value and number of choice
            index = todo_list.index(choice_tick)
            todo_list[index] = "[x]" + choice_tick[3:] #only stuff after the box
            
            complete_list = []
            for item in todo_list:
                if "[x] " in item:
                    complete_list.append(item)
                    todo_list.remove(item)

            for item in complete_list:
                todo_list.append(item)

            reset_txt_list(filepath, todo_list)
            window["list_view"].update(todo_list)
        else:
            pass

    elif user_choice == "clean_list":
        reset_txt_list(filepath, todo_list)        
        clean_list = []

        for item in todo_list:
            if item.startswith("[x]"):
                pass
            else:
                clean_list.append(item)
                #replace todo_list with clean_list to file
        
        todo_list = clean_list
        reset_txt_list(filepath, todo_list)
    
        window["list_view"].update(todo_list)

    # elif user_choice == "switch_button":
    #     user_click, new_filepath = switch_window.read()
    #     print(user_click) #button value / key
    #     print(new_filepath) #all values off all buttons/keys

    #     if user_click == "switch_final":
    #         new_filepath = new_filepath["new_file"]
    #         filepath = str(new_filepath) + ".txt"
    #         todo_list = []  #reset todo_list stored in the program
    #         read_todo_list(filepath) #write new todolist from txt file into the program
    #         switch_window.close()

    #     window["list_view"].update(todo_list)

    
    if user_choice == sg.WIN_CLOSED:
        break



