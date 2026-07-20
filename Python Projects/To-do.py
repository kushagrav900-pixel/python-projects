import customtkinter as tk

# Root window configuration
root = tk.CTk()
root.geometry("300x400+150+100")
root.resizable(True, True)
root.title("To Do list")

frame_root = tk.CTkFrame(root, fg_color="#272727", corner_radius=0)
frame_root.pack(fill="both", expand=True)

# Label
label_task = tk.CTkLabel(frame_root, text="Task List", font=("San Francisco", 20, "bold"), fg_color="#272727", text_color="#C7EBF0")
label_task.pack(side="top",pady=10, padx=10, fill="x")


# Creating Tasks
button_add = tk.CTkButton(frame_root, text="Add Task", font=("San Francisco", 20, "bold"), fg_color="#C7EBF0", text_color="#1A1A1A", hover_color="#A5DFE8", border_width=0, command=lambda: Add())
button_add.pack(side="bottom",pady=10, padx=10, fill="x")


def Add():
    root_add = tk.CTkToplevel(root)
    root_add.geometry("300x200+150+100")
    root_add.resizable(True, True)
    root_add.title("Add Task")

    frame_root_add= tk.CTkFrame(root_add, fg_color="#272727", corner_radius=0)
    frame_root_add.pack(fill="both", expand=True)

    label_add= tk.CTkLabel(frame_root_add, text="Add Task", font=("San Francisco", 20, "bold"), fg_color="#272727", text_color="#C7EBF0")
    label_add.pack(side="top",pady=10, padx=10, fill="x")

    entry_add = tk.CTkEntry(frame_root_add, width=200, height=40, font=("San Francisco", 20, "bold"), fg_color="#C7EBF0", text_color="#1A1A1A", border_width=2)
    entry_add.pack(side="top",pady=10, padx=10, fill="x")

    button_confirm = tk.CTkButton(frame_root_add, text="Add", font=("San Francisco", 20, "bold"), fg_color="#C7EBF0", text_color="#1A1A1A", hover_color="#A5DFE8", border_width=0, command=lambda: Confirmation(entry_add.get()))
    button_confirm.pack(side="bottom",pady=10, padx=10, fill="x")
    
    def Confirmation(a):
        text = a
        tasks = tk.CTkCheckBox(frame_root, text=text, font=("San Francisco", 20, "bold"), fg_color="#272727", text_color="#C7EBF0")
        tasks.pack(side="top",pady=10, padx=10, fill="x")
        root_add.destroy()
    
        




# Mainloop
root.mainloop()