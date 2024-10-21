# Enhanced To-Do List Application

A simple but powerful command-line to-do list application written in Python. This program allows you to manage your tasks efficiently with features like priority, due dates, categories, task search, sorting, and more. 

## Table of Contents

- [How to Run](#how-to-run)
- [Code Breakdown](#code-breakdown)
- [Why a To-Do List Application?](#why-a-to-do-list-application)
- [Future Implementation: Adding a GUI with PyQt](#future-implementation-adding-a-gui-with-pyqt)

---

## How to Run

### Prerequisites

To run the application, ensure that you have Python installed. This project is compatible with **Python 3.6 and above**.

1. **Download and Install Python**:  
   Download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Clone the Repository**:  
   You can download the project by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/Diocese-trees/enhanced_to-do_list.git
   cd enhanced_to-do_list
   ```

3. **Run the Application**:  
   No additional libraries are required. You can directly run the application using:

   ```bash
   python enhancedto-dolist.py
   ```

   Alternatively, if you’re using VS Code or another Python IDE, you can simply run the script from there.

---

## Code Breakdown

Here is a breakdown of all the major functions in the code and how they contribute to the application.

### 1. **Core Task Management Functions**

- **`add_task()`**:  
   Prompts the user to add a new task by entering a description. It then allows the user to optionally add a priority, due date, category, and recurrence for the task. Afterward, the task is saved to the list and persisted in a JSON file.

- **`edit_task()`**:  
   Lets you edit an existing task's details like description, priority, due date, category, and recurrence based on its unique ID.

- **`remove_task()`**:  
   Prompts the user to remove a task by entering its unique task ID.

- **`mark_as_completed()`**:  
   Marks a selected task as completed by entering its ID. This updates the task's status.

- **`view_tasks_without_pause()`**:  
   Displays the list of tasks with details like status (pending or completed), priority, due date, and category.

- **`search_task()`**:  
   Allows the user to search tasks by description, priority, due date, or category. Matches are displayed based on the search criteria.

- **`filter_tasks()`**:  
   Filters the tasks based on their status, i.e., completed or pending.

### 2. **Additional Features**

- **`backup_tasks()`** and **`restore_tasks()`**:  
   These functions allow users to create a backup of all tasks in a separate JSON file and restore them from the backup if needed.

- **`sort_tasks()`**:  
   Sorts tasks based on criteria like task ID, status, priority, or due date.

- **`clear_all_tasks()`**:  
   Deletes all tasks after asking for confirmation, effectively resetting the task list.

- **`display_shortcuts()`**:  
   Displays keyboard shortcuts to make the user experience faster and more convenient.

### 3. **Helper Functions**

- **`save_tasks()`**:  
   Saves the current state of the task list to the `tasks.json` file.

- **`generate_id()`**:  
   Generates a unique ID for each new task by tracking the highest task ID.

- **`validate_due_date()`**:  
   Ensures that due dates are entered in the correct format (`YYYY-MM-DD`).

- **`add_task_priority()`, `add_task_due_date()`, `add_task_category()`, and `add_recurring_task()`**:  
   These functions manage optional task properties, providing flexibility in task creation and management.

---

## Why a To-Do List Application?

### 1. **Organization and Productivity**
A to-do list application helps in organizing your tasks effectively. By breaking down your tasks, setting priorities, and assigning due dates, you can improve your focus and efficiency. A well-managed task list boosts productivity by reducing mental overload and ensuring that important tasks are not forgotten.

### 2. **Track Progress**
The ability to mark tasks as completed provides a sense of accomplishment, motivating you to maintain momentum.

### 3. **Flexibility**
With this enhanced to-do list, tasks can be categorized, sorted, searched, and filtered based on your preferences. This flexibility allows users to adjust the task list to personal workflows.

### 4. **Persistence and Backup**
Tasks are stored in a JSON file, allowing them to persist between sessions. Additionally, you can create backups, ensuring that you never lose your progress.

---

## Future Implementation: Adding a GUI with PyQt

While this application currently runs in the terminal, it can be extended by incorporating a graphical user interface (GUI) using **PyQt5** or **PyQt6**. This would enhance the user experience by allowing drag-and-drop functionality, better navigation, and visual task management.

### Steps for Future Implementation:

1. **Install PyQt**:
   Install PyQt using pip:

   ```bash
   pip install PyQt5
   ```

2. **Design the UI**:
   The user interface can be designed using PyQt Designer, which allows you to visually arrange buttons, fields, and task lists.

3. **Integrate with the Current Code**:
   The existing functions can be linked to the UI components. For example:
   - A button for adding a new task.
   - A list widget to display tasks.
   - Icons or checkboxes to mark tasks as completed.

4. **Features in the GUI**:
   - A calendar view for due dates.
   - Color-coding tasks based on priority.
   - A search bar with real-time filtering.

Implementing a GUI would make the application accessible to a wider audience and easier to use, especially for users unfamiliar with the command line.

---

### Quick Tidbits

- **Command-line simplicity**: While many modern apps are GUI-based, command-line tools are still favored by developers and power users for their speed and simplicity.
- **JSON storage**: JSON makes data storage easy to manage without needing a heavy database.
- **Expandability**: This project can easily be expanded with features like task sharing, cloud backup, or reminders via push notifications.
