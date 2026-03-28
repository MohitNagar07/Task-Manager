# Task Manager Project
# Using: Lists, Functions, While Loops, and Conditionals

todo_list = []
done_list = []

def add_task():
    """Adds a specific number of tasks to the to-do list"""
    print("\n--- Adding Tasks ---")
    print("How many tasks do you want to add?")
    n = int(input("Enter number: "))
    
    while n > 0:
        task = input("Enter task: ")
        todo_list.append(task)
        n = n - 1
    print("Tasks added successfully!")

def done_task():
    """Moves a task from the to-do list to the done list"""
    print("\n--- Mark Task as Done ---")
    s = input("Enter the task you have completed: ")
    
    # Using 'in' to check if it exists before removing
    if s in todo_list:
        todo_list.remove(s)
        done_list.append(s)
        print("Great job! Task moved to Completed.")
    else:
        print("Error: That task is not in your list.")

def show():
    """Prints both lists clearly"""
    print("\n" + "="*20)
    print("YOUR TO-DO LIST:")
    if len(todo_list) == 0:
        print("- (No tasks pending)")
    else:
        for task in todo_list:
            print("- " + task)
            
    print("\nYOUR COMPLETED TASKS:")
    if len(done_list) == 0:
        print("- (No tasks completed yet)")
    else:
        for task in done_list:
            print("- " + task)
    print("="*20 + "\n")

def exits():
    """Final summary before closing the program"""
    print("\nThank you for using Task Manager!")
    show()
    exit()

# Main Program Loop
while True:
    print("Menu:")
    print("1. Add a task")
    print("2. Mark a task as done")
    print("3. Show all tasks")
    print("4. Exit")
    
    choice = int(input("\nEnter your choice (1-4): "))
    
    if choice == 1:
        add_task()
    elif choice == 2:
        done_task()
    elif choice == 3:
        show()
    elif choice == 4:
        exits()
    else:
        print("Invalid choice! Please try again.")


