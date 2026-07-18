import tkinter as tk

# Calculator Window
root = tk.Tk()
root.geometry("310x450+150+100")
root.title("Calc-Postfix")
root.resizable(True, True)

# Creating a frame
frame = tk.Frame(root, bg="#dbfcff", padx=15, pady=15)
frame.pack(fill="both", expand=True)

# Label for Calculator notation
label = tk.Label(frame, text="Calculator", bg="#dbfcff", fg="#1A1A1A", font=("Arial", 20, "bold"))
label.grid(row=0, column=0, columnspan=4, sticky="w")

# Display

text_input = tk.Text(frame, bg="#dbfcff", fg="#1A1A1A", width=12, height=1, font=("Arial", 30, "bold"), highlightthickness=0, highlightbackground="#dbfcff", relief="flat")
text_input.grid(row=1, column=0, columnspan=4)

# Buttons

button_names = ["AC", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "=", ".", "/", "*", "**"]
buttons = []
for k, text in enumerate(button_names):
    
    row = k // 4
    column = k % 4

    button = tk.Button(frame, text=text, width=2, height=1, font=("San Francisco", 30, "bold"), bg="#dbfcff", fg="#1A1A1A", bd=0, highlightthickness=0, highlightbackground="#dbfcff", activebackground="#dbfcff", activeforeground="#a6cfd5",relief="flat", command=lambda t=text: function(t))
    button.grid(row=row + 2, column=column, padx=1, pady=1)
    buttons.append(button)

# Functions
calc = ""

def function(char):
    global calc
    label.configure(text="Calculator")
    if char == "AC":
        calc = ""
        text_input.delete(1.0, tk.END)
    elif char != "=":
        calc += char
        text_input.delete(1.0, tk.END)
        text_input.insert(1.0, calc)
    elif char == "=":
        try:
            calc = tokenize(calc)
        except Exception as e:
            print(e)
            label.configure(text="Error")
            raise
        text_input.delete(1.0, tk.END)
        text_input.insert(1.0, calc)    

# Tokenisation

def tokenize(calc):
    tokens_operator = []
    tokens_digit = []
    current_number = ""
    i = 0
    while i < len(calc):
        character = str(calc[i])
        if character.isdigit() or character == ".":
            current_number += character
        else:
            tokens_digit.append(current_number)
            current_number = ""
            if character == "*" and calc[i + 1] == "*":
                tokens_operator.append("**")
                i = i + 1
            else:
                tokens_operator.append(character)  

        i = i + 1
    if current_number:
        tokens_digit.append(current_number)

    postfix_list = tokens_digit
    postfix_list.extend(tokens_operator[::-1])
    
    j = 0
    first_num = postfix_list[0]
    while j < len(tokens_operator):
        
        if postfix_list[len(postfix_list) - j - 1] == "+":
            first_num = float(first_num) + float(postfix_list[j + 1])
        elif postfix_list[len(postfix_list) - j - 1] == "-":
            first_num = float(first_num) - float(postfix_list[j + 1])
        elif postfix_list[len(postfix_list) - j - 1] == "*":
            first_num = float(first_num) * float(postfix_list[j + 1])
        elif postfix_list[len(postfix_list) - j - 1] == "/":
            first_num = float(first_num) / float(postfix_list[j + 1])
        elif postfix_list[len(postfix_list) - j - 1] == "**":
            first_num = float(first_num) ** float(postfix_list[j + 1])
        j = j + 1
    calc = str(first_num)
    text_input.delete(1.0, tk.END)
    text_input.insert(1.0, calc)
    return calc    
        
    
    
# Mainloop
root.mainloop()