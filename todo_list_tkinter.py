# todo_list_tkinter.py

import tkinter as tk
from tkinter import messagebox
import os

TASK_FILE = "tasks.txt"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        self.tasks = []

        title = tk.Label(
            root,
            text="To-Do List",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.task_entry = tk.Entry(frame, width=28, font=("Arial", 14))
        self.task_entry.grid(row=0, column=0, padx=5)

        add_button = tk.Button(
            frame,
            text="Add Task",
            width=10,
            command=self.add_task
        )
        add_button.grid(row=0, column=1)

        list_frame = tk.Frame(root)
        list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            list_frame,
            width=45,
            height=18,
            font=("Arial", 12),
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            width=12,
            command=self.delete_task
        )
        delete_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(
            button_frame,
            text="Mark Complete",
            width=12,
            command=self.mark_complete
        )
        complete_button.grid(row=0, column=1, padx=5)

        save_button = tk.Button(
            button_frame,
            text="Save Tasks",
            width=12,
            command=self.save_tasks
        )
        save_button.grid(row=0, column=2, padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            width=12,
            command=self.clear_tasks
        )
        clear_button.grid(row=1, column=0, columnspan=3, pady=8)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)

            if not task.startswith("✅ "):
                completed_task = "✅ " + task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, completed_task)
                self.tasks[selected_index] = completed_task
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark complete.")

    def save_tasks(self):
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        self.tasks.append(task)
                        self.task_listbox.insert(tk.END, task)