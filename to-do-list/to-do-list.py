import os

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1] += " (completed)"
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number.")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice.")

main()
