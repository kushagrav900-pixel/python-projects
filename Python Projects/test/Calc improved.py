import tkinter as tk

# Initialize main window
root = tk.Tk()
root.geometry("380x520+150+100")
root.minsize(300, 450)
root.title("Calculator")
root.configure(bg="#0f172a")

# Global calculation string and error state
calc = ""
error_state = False

# Master frame with padding
frame = tk.Frame(root, bg="#0f172a", padx=15, pady=15)
frame.pack(fill="both", expand=True)

# Status / Title Label
status_label = tk.Label(
    frame, 
    text="Calculator", 
    bg="#0f172a", 
    fg="#38bdf8", 
    font=("Arial", 12, "bold")
)
status_label.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky="w")

# Display Entry Widget (Disabled direct user input, right aligned)
display = tk.Entry(
    frame,
    bg="#1e293b",
    fg="#ffffff",
    font=("Arial", 28),
    bd=0,
    justify="right",
    insertbackground="#ffffff",
    relief="flat",
    highlightthickness=2,
    highlightbackground="#334155",
    highlightcolor="#38bdf8"
)
display.grid(row=1, column=0, columnspan=4, ipady=12, padx=2, pady=(0, 15), sticky="nsew")

# Block keyboard typing in the entry directly to preserve clean output formatting
display.bind("<Key>", lambda e: "break")

# Helper functions
def update_display():
    # Show user-friendly × and ÷ instead of * and /
    display_text = calc.replace("*", "×").replace("/", "÷")
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, display_text)
    display.config(state="readonly")
    display.xview_moveto(1.0)

def add_to_expression(symbol):
    global calc, error_state
    if error_state:
        status_label.config(text="Calculator", fg="#38bdf8")
        error_state = False
        calc = ""
    calc += str(symbol)
    update_display()

def evaluate_expression():
    global calc, error_state
    if not calc:
        return
    try:
        # Safe evaluation since we only allow sanitized mathematical inputs
        result = eval(calc)
        
        # Convert whole number floats (e.g. 5.0) to integers
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        calc = str(result)
        status_label.config(text="Calculator", fg="#38bdf8")
        error_state = False
    except Exception:
        status_label.config(text="ERROR", fg="#ef4444")
        error_state = True
        # Keep calc unchanged so the user can backspace to edit the formula
    update_display()

def clear_expression():
    global calc, error_state
    status_label.config(text="Calculator", fg="#38bdf8")
    error_state = False
    calc = ""
    update_display()

def backspace():
    global calc, error_state
    if error_state:
        status_label.config(text="Calculator", fg="#38bdf8")
        error_state = False
    else:
        calc = calc[:-1]
    update_display()

def on_button_click(char):
    if char == "=":
        evaluate_expression()
    elif char == "C":
        clear_expression()
    elif char == "⌫":
        backspace()
    else:
        add_to_expression(char)

def on_key_press(event):
    char = event.char
    keysym = event.keysym
    
    # Map keyboard input
    if char in "0123456789+-*/().":
        add_to_expression(char)
    elif char.lower() == "x":
        add_to_expression("*")
    elif keysym in ("Return", "KP_Enter") or char == "=":
        evaluate_expression()
    elif keysym == "BackSpace":
        backspace()
    elif keysym == "Escape" or char.lower() == "c":
        clear_expression()

# Keyboard Binding
root.bind("<Key>", on_key_press)

# Button styling configuration
styles = {
    "num": {
        "bg": "#1e293b", "fg": "#f8fafc", "hover": "#334155"
    },
    "op": {
        "bg": "#0284c7", "fg": "#f8fafc", "hover": "#38bdf8"
    },
    "special": {
        "bg": "#475569", "fg": "#f8fafc", "hover": "#64748b"
    },
    "eq": {
        "bg": "#059669", "fg": "#f8fafc", "hover": "#10b981"
    }
}

# Grid Layout setup (row, column, category style)
buttons_layout = [
    ("C", 2, 0, "special"), ("(", 2, 1, "special"), (")", 2, 2, "special"), ("⌫", 2, 3, "special"),
    ("7", 3, 0, "num"),     ("8", 3, 1, "num"),     ("9", 3, 2, "num"),     ("/", 3, 3, "op"),
    ("4", 4, 0, "num"),     ("5", 4, 1, "num"),     ("6", 4, 2, "num"),     ("*", 4, 3, "op"),
    ("1", 5, 0, "num"),     ("2", 5, 1, "num"),     ("3", 5, 2, "num"),     ("-", 5, 3, "op"),
    ("0", 6, 0, "num"),     (".", 6, 1, "num"),     ("=", 6, 2, "eq"),      ("+", 6, 3, "op"),
]

# Create hover binding helper
def bind_hover(widget, normal_bg, hover_bg):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg))

# Create and grid buttons
for text, row, col, style_name in buttons_layout:
    style = styles[style_name]
    btn_text = "×" if text == "*" else ("÷" if text == "/" else text)
    
    btn = tk.Button(
        frame,
        text=btn_text,
        font=("Arial", 16, "bold"),
        bg=style["bg"],
        fg=style["fg"],
        activebackground=style["hover"],
        activeforeground="#ffffff",
        bd=0,
        relief="flat",
        command=lambda t=text: on_button_click(t)
    )
    bind_hover(btn, style["bg"], style["hover"])
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# Configure resizing weights
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

frame.rowconfigure(0, weight=0)
frame.rowconfigure(1, weight=0)
for r in range(2, 7):
    frame.rowconfigure(r, weight=1)

# Initialize display values
update_display()

# Main Loop
root.mainloop()
