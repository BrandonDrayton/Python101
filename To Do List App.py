# Todo List App Using Dictionaries
# In this exercise you are going to create a Todo List App. Create a new folder and initialize it as a git repository. Connect the repository up to github and make sure you commit and push your changes as you work through the solution.

# Features:
# When the app starts it should present user with the following menu:




todo_list = []
task = ()

while True:
    menu = input("Press 1 to add task: \n" 
    "Press 2 to delete task: \n" 
    "Press 3 to view all tasks: \n" 
    "Press q to quit: \n")
    if menu == str(1):
        task = input("What is the name of your task? ")
        priority = input("Is your task priority low, medium, or hard? ")  
        todo_list[task]=priority
        print(todo_list)
        task_validation = input("Is this correct? ")
        if task_validation == "No" or "no":
            del todo_list
            print(todo_list)
        if task_validation == "Yes" or "yes":
            print(todo_list)
    elif menu == str(2):
        print(todo_list)
        task_del = input("Which task do you wish to delete? ")
        del todo_list[task_del]
    elif menu == str(3):
        print(todo_list)
    
    
    elif menu == 'q':
        break
    
        







# Add Task:
# Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low. Make sure you validate this.

# Delete Task:
# Show user all the tasks along with the index number of each task. User can then enter the index number of the task to delete the task.

# View all tasks:
# Allow the user to view all the tasks in the following format:

# 1 - Wash the car - high
# 2 - Mow the lawn - low
# Implementation Suggestions
# Store each task in a dictionary and use 'title' and 'priority' as keys of the dictionary.

# Store each dictionary inside an array. Array will represent list of tasks.