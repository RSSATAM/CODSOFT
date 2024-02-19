import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_task():
    selected_task_index = listbox.curselection()
    updated_task = entry.get()
    if selected_task_index and updated_task:
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, updated_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task and enter an update!")

def complete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.itemconfig(selected_task_index, {'bg': 'light blue'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

#Main window
root = tk.Tk()
root.title("To-Do List App")

# Create widgets
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

# Run the main loop
root.mainloop()

