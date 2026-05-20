import json
import os
class Task:
    def __init__(self, name):
        self.name = name
        self.status = False


tasks = []
if os.path.isfile("tasks.json") and os.path.getsize("tasks.json") > 0:
    with open("tasks.json", "r") as file:
        data = json.load(file)

    for item in data:
        task = Task(item["name"])
        task.status = item["status"]
        tasks.append(task)

def menu():
    print("""
===== TO-DO LIST MENU =====
    1. Add Task
    2. View Tasks
    3. Mark Task Completed
    4. Delete Task
    5. Exit
    """)
def show_task():
    if not tasks:
        print("No task added yet ..........")
    else:    
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task.status else " "
            print(f"{i}. [{status}] {task.name}")

while(True):
    menu()
    a = int(input("Enter the choice : "))
    match a:
        case 1:
            tasks.append(Task(input("Enter the name of the new task : ")))

        case 2:
            show_task()


        case 3:
            tasks[int(input("Enter the number of the task completed : ")) - 1].status = True
            show_task()
        case 4:
            if not tasks:
                print("No tasks to delete")
            else:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        deleted_task = tasks.pop(task_num - 1)
                        print(f"Deleted: {deleted_task.name}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a valid number")
            show_task()
        case 5:
            with open("tasks.json", "w") as file:
                data = [{"name": task.name, "status": task.status} for task in tasks]
                json.dump(data, file, indent=4)
            print("Exit")
            break
    print("Press any key to continue...")
    input("")




            