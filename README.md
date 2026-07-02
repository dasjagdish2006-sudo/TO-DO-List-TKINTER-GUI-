# To-Do List App (Tkinter)

A desktop To-Do List application built with Python's Tkinter GUI library, allowing users to add, complete, delete, and save tasks.

## Features

- Add new tasks via a text entry field
- Mark tasks as complete (adds a ✅ checkmark)
- Delete selected tasks
- Clear all tasks at once
- Save tasks to a local file (`tasks.txt`)
- Automatically loads saved tasks on startup
- Scrollable task list

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)

## Usage

```bash
python todo_list_tkinter.py
```

1. Type a task into the input field and click **Add Task**.
2. Select a task and click **Mark Complete**, **Delete Task**, or **Clear All** as needed.
3. Click **Save Tasks** to store your list in `tasks.txt` for next time.

## Notes

- Tasks are only persisted to `tasks.txt` when you click **Save Tasks**.
- The `tasks.txt` file is created automatically in the same directory as the script.
