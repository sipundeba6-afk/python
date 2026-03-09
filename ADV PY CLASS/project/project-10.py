tasks = []

def add_task():
    task=input("Enter task: ")
    deadline=input("Enter deadline: ")
    priority=input("Enter priority: ")
    tasks.append((task, deadline, priority))
    print("Task added!")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        for t in tasks:
            print("Task:", t[0], "Deadline:", t[1], "Priority:", t[2])

while True:
    print("\n1.Add Task")
    print("2.Show Tasks")
    print("3.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        break
