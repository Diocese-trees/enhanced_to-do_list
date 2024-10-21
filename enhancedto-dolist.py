import json
import os
import time
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"
# Initialize tasks list
tasks = []

# Track the highest ID assigned to avoid duplicate IDs when tasks are removed
max_task_id = 0

# Load existing tasks from file (if any)
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
        max_task_id = max(task['id'] for task in tasks)

# Function to save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to generate unique ID
def generate_id():
    global max_task_id
    max_task_id += 1
    return max_task_id

# Function to check if task already exists
def task_already_exists(description):
    return any(task["description"].lower() == description.lower() for task in tasks)

# Function to validate due date input
def validate_due_date():
    while True:
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

# Function to add task priority (if chosen)
def add_task_priority(task):
    while True:
        priority_choice = input("Would you like to add a priority? (yes/no): ").lower()
        if priority_choice == "yes":
            print("Select Task Priority:")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            choice = input("Enter your choice: ")
            task["priority"] = {"1": "High", "2": "Medium"}.get(choice, "Low")
            break
        elif priority_choice == "no":
            task["priority"] = "Low"  # Default priority
            break
        else:
            print("Invalid input. Please try again.")

# Function to add task due date (if chosen)
def add_task_due_date(task):
    while True:
        due_date_choice = input("Would you like to add a due date? (yes/no): ").lower()
        if due_date_choice == "yes":
            task["due_date"] = validate_due_date()
            break
        elif due_date_choice == "no":
            task["due_date"] = None  # No due date
            break
        else:
            print("Invalid input. Please try again.")

# Function to add task category (optional)
def add_task_category(task):
    while True:
        category_choice = input("Would you like to add a category? (yes/no): ").lower()
        if category_choice == "yes":
            category = input("Enter a category for this task (e.g., work, personal, urgent): ")
            task["category"] = category
            break
        elif category_choice == "no":
            task["category"] = None  # No category
            break
        else:
            print("Invalid input. Please try again.")

# Function to add recurring task (optional)
def add_recurring_task(task):
    while True:
        recurring_choice = input("Is this a recurring task? (yes/no): ").lower()
        if recurring_choice == "yes":
            task["recurrence"] = input("How often does it recur? (daily, weekly, monthly): ").lower()
            break
        elif recurring_choice == "no":
            task["recurrence"] = None  # No recurrence
            break
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")

# Function to add a new task
def add_task():
    clear_screen()
    print("Add a new task")
    description = input("Enter the task description: ")

    # Check if the task already exists
    if task_already_exists(description):
        print("This task already exists.")
        input("Press Enter to return to the menu...")
        return

    # Create the task with a unique ID
    task = {
        "id": generate_id(),
        "description": description,
        "status": "pending"  # Default status
    }

    # Allow adding optional details
    add_task_priority(task)
    add_task_due_date(task)
    add_task_category(task)
    add_recurring_task(task)

    # Save the task to the list and file
    tasks.append(task)
    save_tasks()

    print(f"Task '{description}' has been added!")
    input("Press Enter to return to the menu...")

# Function to mark task as completed
def mark_as_completed():
    while True:
        clear_screen()
        view_tasks_without_pause()
        try:
            task_id_to_complete = int(input("Enter the ID of the task to mark as completed: "))
            for task in tasks:
                if task["id"] == task_id_to_complete:
                    if task.get("status") == "completed":
                        print(f"Task with ID #{task_id_to_complete} is already completed.")
                    else:
                        task["status"] = "completed"
                        save_tasks()
                        print(f"Task with ID #{task_id_to_complete} has been marked as completed.")
                    break
            else:
                print(f"Task with ID #{task_id_to_complete} not found.")
        except ValueError:
            print("Invalid input.")

        next_action = redo_action_prompt()
        if next_action == "menu":
            break
        elif next_action == "different":
            return

# Function to edit task
def edit_task():
    while True:
        clear_screen()
        view_tasks_without_pause()
        try:
            task_id_to_edit = int(input("Enter the ID to edit: "))
            for task in tasks:
                if task["id"] == task_id_to_edit:
                    task["description"] = input("Enter the new task description: ")
                    add_task_priority(task)  # Allow editing the priority
                    add_task_due_date(task)   # Allow editing the due date
                    add_task_category(task)    # Allow editing the category
                    add_recurring_task(task)    # Allow editing recurrence
                    save_tasks()
                    print(f"Task with ID #{task_id_to_edit} has been updated.")
                    break
            else:
                print(f"Task with ID #{task_id_to_edit} not found.")
        except ValueError:
            print("Invalid input.")

        next_action = redo_action_prompt()
        if next_action == "menu":
            break
        elif next_action == "different":
            return
        elif next_action == "continue":
            return

# Function to remove a task
def remove_task():
    while True:
        clear_screen()
        view_tasks_without_pause()
        try:
            task_id_to_remove = int(input("Enter the ID of the task to remove: "))
            for task in tasks:
                if task["id"] == task_id_to_remove:
                    tasks.remove(task)
                    save_tasks()
                    print(f"Task with ID #{task_id_to_remove} has been removed.")
                    return
            print(f"Task with ID #{task_id_to_remove} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")

        next_action = redo_action_prompt()
        if next_action == "menu":
            break
        elif next_action == "different":
            return

# Function to search tasks
def search_task():
    clear_screen()
    search_by = input("Search by (description/priority/due_date/category): ").lower()
    if search_by == "description":
        keyword = input("Enter a keyword to search in descriptions: ")
        found_tasks = [task for task in tasks if keyword.lower() in task["description"].lower()]
    elif search_by == "priority":
        priority = input("Enter priority to search (High/Medium/Low): ")
        found_tasks = [task for task in tasks if task.get("priority", "").lower() == priority.lower()]
    elif search_by == "due_date":
        date = validate_due_date()
        found_tasks = [task for task in tasks if task.get("due_date", "") == date]
    elif search_by == "category":
        category = input("Enter category to search: ")
        found_tasks = [task for task in tasks if task.get("category", "").lower() == category.lower()]
    else:
        found_tasks = []

    if found_tasks:
        print("Search Results:")
        for task in found_tasks:
            status = "✅ Completed" if task.get("status") == "completed" else "❌ Pending"
            priority = task.get("priority", "Not Set")
            due_date = task.get("due_date", "Not Set")
            category = task.get("category", "Not Set")
            recurrence = task.get("recurrence", "None")
            print(f"ID #{task['id']}: {task['description']} - {status} | Priority: {priority} | Due Date: {due_date} | Category: {category} | Recurrence: {recurrence}")
    else:
        print("No tasks found matching the criteria.")
    input("Press Enter to return to the menu...")

# Function to filter tasks by status
def filter_tasks():
    status_choice = input("Filter tasks by (completed/pending): ").lower()
    if status_choice == "completed":
        filtered_tasks = [task for task in tasks if task.get("status") == "completed"]
    elif status_choice == "pending":
        filtered_tasks = [task for task in tasks if task.get("status") != "completed"]
    else:
        print("Invalid input.")
        return

    if filtered_tasks:
        for task in filtered_tasks:
            status = "✅ Completed" if task.get("status") == "completed" else "❌ Pending"
            print(f"ID #{task['id']}: {task['description']} - {status}")
    else:
        print(f"No {status_choice} tasks found.")
    input("Press Enter to return to the menu...")

# Function to view task details by ID
def view_task_details():
    clear_screen()
    view_tasks_without_pause()  # Show available tasks
    try:
        task_id = int(input("Enter the ID of the task to view details: "))
        for task in tasks:
            if task["id"] == task_id:
                status = "✅ Completed" if task.get("status") == "completed" else "❌ Pending"
                print(f"\nTask ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Status: {status}")
                print(f"Priority: {task.get('priority', 'Not Set')}")
                print(f"Due Date: {task.get('due_date', 'Not Set')}")
                print(f"Category: {task.get('category', 'Not Set')}")
                print(f"Recurrence: {task.get('recurrence', 'None')}")
                break
        else:
            print(f"Task with ID #{task_id} not found.")
    except ValueError:
        print("Invalid input.")
    input("Press Enter to return to the menu...")

# Sort Tasks by ID, Status, Priority, or Due Date
def sort_tasks():
    clear_screen()
    print("Sort tasks by:")
    print("1. ID")
    print("2. Status")
    print("3. Priority")
    print("4. Due Date")

    sort_by = input("Enter your choice: ")

    if sort_by == "1":
        tasks.sort(key=lambda task: task["id"])
    elif sort_by == "2":
        tasks.sort(key=lambda task: task.get("status", "pending"))
    elif sort_by == "3":
        tasks.sort(key=lambda task: task.get("priority", "Low"))
    elif sort_by == "4":
        tasks.sort(key=lambda task: task.get("due_date", "Not Set"))
    else:
        print("Invalid choice. Please select a valid sorting option.")

# Backup Tasks
def backup_tasks():
    backup_file = "tasks_backup.json"
    with open(backup_file, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks have been backed up to {backup_file}.")
    input("Press Enter to return to the menu...")

# Restore Tasks
def restore_tasks():
    backup_file = "tasks_backup.json"
    global tasks
    if os.path.exists(backup_file):
        with open(backup_file, "r") as file:
            tasks = json.load(file)
        print("Tasks restored from backup.")
    else:
        print(f"No backup file found at {backup_file}.")
    input("Press Enter to return to the menu...")

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to view tasks without pause
def view_tasks_without_pause():
    clear_screen()
    if not tasks:
        print("No tasks available.")
        return
    print("Current Tasks:")
    for task in tasks:
        status = "✅ Completed" if task.get("status") == "completed" else "❌ Pending"
        priority = task.get("priority", "Not Set")
        due_date = task.get("due_date", "Not Set")
        category = task.get("category", "Not Set")
        recurrence = task.get("recurrence", "None")
        print(f"ID #{task['id']}: {task['description']} - {status} | Priority: {priority} | Due Date: {due_date} | Category: {category} | Recurrence: {recurrence}")

# Function to prompt for an action after completing an operation
def redo_action_prompt():
    while True:
        choice = input("Do you want to return to the menu or perform another action? (menu/different/continue): ").lower()
        if choice in ["menu", "different", "continue"]:
            return choice
        else:
            print("Invalid input. Please enter 'menu', 'different', or 'continue'.")

# Function to clear all tasks
def clear_all_tasks():
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks()
        print("All tasks have been cleared.")
    else:
        print("Task clearing aborted.")
    input("Press Enter to return to the menu...")

# Function to display keyboard shortcuts
def display_shortcuts():
    clear_screen()
    print("Keyboard Shortcuts:")
    print("1. Add Task - 'a'")
    print("2. View Tasks - 'v'")
    print("3. Remove Task - 'r'")
    print("4. Mark as Completed - 'c'")
    print("Press the respective key to perform the action directly.")
    input("Press Enter to return to the menu...")

# Main Loop with Keyboard Shortcuts
if __name__ == "__main__":
    print("Welcome to the Enhanced To-Do List App :)")
    while True:
        clear_screen()
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Edit a task")
        print("6. Search tasks")
        print("7. Filter tasks by status")
        print("8. Clear all tasks")
        print("9. Sort tasks")
        print("10. View task details")
        print("11. Backup tasks")
        print("12. Restore tasks")
        print("13. Display Keyboard Shortcuts")
        print("14. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks_without_pause()
            input("Press Enter to return to the menu...")
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_as_completed()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            search_task()
        elif choice == '7':
            filter_tasks()
        elif choice == '8':
            clear_all_tasks()
        elif choice == '9':
            sort_tasks()
        elif choice == '10':
            view_task_details()
        elif choice == '11':
            backup_tasks()
        elif choice == '12':
            restore_tasks()
        elif choice == '13':
            display_shortcuts()
        elif choice == '14':
            clear_screen()
            print("Thank you for using this program to keep track of your daily goals. Goodbye 👋👋")
            break
        else:
            clear_screen()
            print("Invalid input. Please try again.")
            time.sleep(2)
