import tkinter as tk
from tkinter import messagebox


def add_todo():
    todo_item = entry.get()
    if todo_item:
        listbox.insert(tk.END, todo_item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a todo item.")

def update_todo():
    selected_index = listbox.curselection()
    if selected_index:
        todo_item = entry.get()
        if todo_item:
            listbox.delete(selected_index)
            listbox.insert(selected_index, todo_item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a todo item.")
    else:
        messagebox.showwarning("Warning", "Please select a todo item to update.")

def remove_todo():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a todo item to remove.")

def mark_completed():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.itemconfig(selected_index, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a todo item to mark as completed.")

def clear_todos():
    listbox.delete(0, tk.END)

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("Todo List Application")

    # Entry for adding/updating todo
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    # Buttons
    add_button = tk.Button(root, text="Add Todo", command=add_todo)
    add_button.pack(side=tk.LEFT, padx=5)

    update_button = tk.Button(root, text="Update Todo", command=update_todo)
    update_button.pack(side=tk.LEFT, padx=5)

    remove_button = tk.Button(root, text="Remove Todo", command=remove_todo)
    remove_button.pack(side=tk.LEFT, padx=5)

    mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
    mark_completed_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(root, text="Clear All", command=clear_todos)
    clear_button.pack(side=tk.LEFT, padx=5)

    # Todo List
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
