import tkinter as tk

# Calculator
root = tk.Tk()
root.geometry("600x400+150+100")
root.title("Calculator")
root.resizable(True, True)

# Framing
frame = tk.Frame(root, bg="#1A1A1A", padx=15, pady=15)
frame.pack(fill="both", expand=True)

# Label
Label = tk.Label(frame, text="Calculator", bg="#1A1A1A", fg="lightblue", font=("Arial", 20, "bold"))

Label.grid(row=0, column=0)

# Text
text = tk.Text(frame, bg="#1A1A1A", width=16, height=1, font=("Arial", 30), bd=0, highlightbackground="#1A1A1A", relief="flat")
text.config(state="disabled")
text.grid(columnspan=4, row=1)

# calculation string

calc = ""

# Functions

def update_display():
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.insert("1.0", calc)
    text.config(state="disabled")

def function(symbol):
    Label.config(text="Calculator", fg="lightblue")
    global calc
    calc += str(symbol)
    update_display()


def equivalent():
    global calc
    try:
        calc = str(eval(calc))
        update_display()
    except Exception:
        Label.config(text="ERROR", fg="red")
        calc = ""
        update_display()
def clearing():
    Label.config(text="Calculator",fg="lightblue")
    global calc
    calc = ""
    update_display()
    

# Buttons
plus = tk.Button(frame, width=2, height=1, text="+", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("+"))
plus.grid(row=2,column=0)

minus = tk.Button(frame, width=2, height=1, text="-", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("-"))
minus.grid(row=2,column=1)

division = tk.Button(frame, width=2, height=1, text="/", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("/"))
division.grid(row=2,column=2)

multiplication = tk.Button(frame, width=2, height=1, text="*", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("*"))
multiplication.grid(row=2,column=3)

one = tk.Button(frame, width=2, height=1, text="1", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("1"))
one.grid(row=3,column=0)

two = tk.Button(frame, width=2, height=1, text="2", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("2"))
two.grid(row=3,column=1)

three = tk.Button(frame, width=2, height=1, text="3", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("3"))
three.grid(row=3,column=2)

four = tk.Button(frame, width=2, height=1, text="4", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("4"))
four.grid(row=3,column=3)

five = tk.Button(frame, width=2, height=1, text="5", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("5"))
five.grid(row=4,column=0)

six = tk.Button(frame, width=2, height=1, text="6", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("6"))
six.grid(row=4,column=1)

seven = tk.Button(frame, width=2, height=1, text="7", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("7"))
seven.grid(row=4,column=2)

eight = tk.Button(frame, width=2, height=1, text="8", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("8"))
eight.grid(row=4,column=3)

nine = tk.Button(frame, width=2, height=1, text="9", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("9"))
nine.grid(row=5,column=0)

zero = tk.Button(frame, width=2, height=1, text="0", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=lambda: function("0"))
zero.grid(row=5,column=1)

equate = tk.Button(frame, width=2, height=1, text="=", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=equivalent)
equate.grid(row=5, column=2)

clear = tk.Button(frame, width=2, height=1, text="C", font=("Arial", 30), bg="#1A1A1A", bd=0, highlightbackground="#1A1A1A", relief="flat", activebackground="#2A2A2A", activeforeground="lightblue", command=clearing)
clear.grid(row=5, column=3)






# Frame Configure
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)



# Mainloop
root.mainloop()