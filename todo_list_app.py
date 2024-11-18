import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App by Sumayyah Al-Zanbahi")
        self.root.geometry("400x500")

        # Task list
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List by Sumayyah Al-Zanbahi", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Add Button
        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Buttons for Actions
        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 12), command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        """Add a task to the list"""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        """Delete the selected task from the list"""
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        """Clear all tasks from the list"""
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
