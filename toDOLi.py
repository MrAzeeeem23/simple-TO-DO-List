def show_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{idx}. [{status}] {task['task']}")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_idx]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to delete: ")) - 1
        deleted_task = tasks.pop(task_idx)
        print(f"Deleted task: {deleted_task['task']}")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")


if __name__ == "__main__":
    main()
