import tkinter as tk

# Calculator
root = tk.Tk()
root.geometry("600x400+150+100")
root.title("Calculator")
root.resizable(True, True)

# Framing
frame = tk.Frame(root, bg="#1A1A1A")
frame.config()
frame.pack(fill="both", expand=True)

# Label
Label = tk.Label(frame, text="Calculator", bg="#1A1A1A", fg="lightblue", font=("Arial", 20))
Label.grid(row=0, column=0, columnspan=4)

# Text
text = tk.Text(frame, bg="#1A1A1A", width=16, height=1, font=("Arial", 30), bd=0, highlightbackground="#1A1A1A", relief="flat")
text.config(state="disabled")
text.grid(columnspan=4, row=1)

# calculation string

calc = ""


# Buttons
plus = tk.Button(frame, width=2, height=1, text="+", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", command=lambda: function("+"))
plus.grid(row=2,column=0)

minus = tk.Button(frame, width=2, height=1, text="-", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", command=lambda: function("-"))
minus.grid(row=2,column=1)

division = tk.Button(frame, width=2, height=1, text="/", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", command=lambda: function("/"))
division.grid(row=2,column=2)

multiplication = tk.Button(frame, width=2, height=1, text="*", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", command=lambda: function("*"))
multiplication.grid(row=2,column=3)


def function(symbol):
    global calc
    calc += str(symbol)
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.insert("1.0", calc)
    text.config(state="disabled")


# Frame Configure
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)



# Mainloop
root.mainloop()