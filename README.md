# ToDo List Program

Welcome to the ToDo List program! This program provides a command-line interface (CLI) version and a graphical user interface (GUI) version for managing your tasks and to-do lists. It is built using Python and demonstrates various functionalities such as adding, editing, marking tasks as completed, and more.

## Functionalities

### CLI Version
![](https://github.com/xAmiBa/To_Do/blob/main/screenshots/Screenshot%202023-08-21%20at%2023.38.48.png)
1. **Add**: Add a new task to the list.
2. **Tick**: Mark a task as completed.

![](https://github.com/xAmiBa/To_Do/blob/main/screenshots/Screenshot%202023-08-21%20at%2023.39.13.png)

4. **Edit**: Edit an existing task.
5. **Show**: Display the current tasks in the list.
6. **Switch**: Switch between different to-do lists.
7. **New List**: Create a new to-do list.
8. **Cleanup**: Remove completed tasks from the list.
9. **Menu**: Display the menu options.
10. **Exit**: Exit the program.

### GUI Version
![image](https://github.com/xAmiBa/To_Do/blob/main/screenshots/Screenshot%202023-08-21%20at%2023.37.55.png)
1. **Add**: Add a new task to the list.
2. **Tick**: Mark a task as completed.
   
![](https://github.com/xAmiBa/To_Do/blob/main/screenshots/Screenshot%202023-08-21%20at%2023.38.03.png)

4. **Edit**: Edit an existing task.
5. **Cleanup**: Remove completed tasks from the list.

![](https://github.com/xAmiBa/To_Do/blob/main/screenshots/Screenshot%202023-08-21%20at%2023.38.13.png)

## Libraries Used

The program utilizes the following libraries:
- `PySimpleGUI`: For building the graphical user interface in the GUI version.
- Standard Python libraries for file handling and input/output operations.

## How the Program Works

### CLI Version

1. The program starts by checking if the specified to-do list file exists. If it doesn't exist, the program creates a new list or prompts the user to provide a valid file.
2. After loading the list, the program displays the main menu and the current tasks.
3. The user can select options from the menu, such as adding, editing, and marking tasks as completed.
4. The program updates the to-do list file after each modification to maintain the tasks.

### GUI Version

1. The program starts by loading the default to-do list file.
2. The GUI displays the list of tasks and input fields for adding and editing tasks.
3. Users can interact with buttons to perform actions like adding, editing, and marking tasks as completed.
4. The GUI updates the list display and the underlying file when tasks are modified.
5. Users can exit the GUI by closing the window.

## What I Learned

In the process of building this ToDo List program, I gained valuable experience in several areas:

- Utilizing Python to create a functional command-line application and graphical user interface (GUI) program.
- Designing **modular code by creating separate modules for functions and variables**.
- Implementing **functions** to encapsulate specific tasks, such as printing menus, reading and writing to-do lists, and more.
- Understanding the benefits of using functions, such as code reusability and better organization.
- Creating and using **global variables** to maintain state across different parts of the program.
- Learning how to handle user input and create interactive menu systems.
- Incorporating **file handling operations** to store and retrieve task data in **text files**.
- Enhancing my problem-solving skills by addressing **user input validation** and managing program flow.
- Developing a graphical user interface (GUI) using the **PySimpleGUI library**.


## Future Developments

- Web App version
- Sending finished todo list through email
