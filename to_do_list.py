class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            print(f"Task '{task}' marked as completed.")
            # Optionally, you can move completed tasks to a separate list or remove them entirely.
        else:
            print("Invalid task index. Please enter a valid index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted from the to-do list.")
        else:
            print("Invalid task index. Please enter a valid index.")

def todo_list_app():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Example: Run the to-do list app
todo_list_app()
