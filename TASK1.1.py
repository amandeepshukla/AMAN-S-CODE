class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        print(f"Task '{description}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['description']} - {status}")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"Task {index} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task['description']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: "))
            todo_list.complete_task(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()