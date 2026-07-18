import subprocess
import tkinter as tk

# GUI sectiion

root = tk.Tk()
root.title("Postfix Calculator")
root.geometry("310x450+150+100")
root.resizable(True, True)

frame = tk.Frame(root, bg="#EAF0CE")
frame.pack(fill="both", expand=True)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

Label = tk.Label(frame, text="Postfix Calculator", bg="#EAF0CE", fg="#1A1A1A", font=("San Francisco", 20, "bold"))
Label.grid(row=0, column=0, columnspan=4, sticky="w")

text_entry = tk.Text(frame, bg="#EAF0CE", fg="#1A1A1A", width=12, height=1, font=("San Francisco", 30, "bold"), highlightthickness=0, highlightbackground="#EAF0CE", relief="flat")
text_entry.grid(row=1, column=0, columnspan=4, sticky="nsew")

buttons_list = ["AC", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "=", ".", "/", "*", "**"]
buttons = []
for k, text in enumerate(buttons_list):
    row = k // 4
    column = k % 4
    button = tk.Button(frame, text=text, width=2, height=1, font=("San Francisco", 30, "bold"), bg="#EAF0CE", fg="#1A1A1A", bd=0, highlightthickness=0, highlightbackground="#EAF0CE", activebackground="#EAF0CE", activeforeground="#a6cfd5",relief="flat", command=lambda t=text: function(t))
    button.grid(row=row + 2, column=column, padx=1, pady=1)
    buttons.append(button)

expression = ""
def function(char):
    global expression
    if char == "AC":
        expression = ""
        update_output(expression)
    elif char == "=":
        pass
    else:
        expression += char
        update_output(expression)

def tokenisation():
    global expression
    tokens_list = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == ".":
            current_number = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                current_number += expression[i]
                i += 1
        
            tokens_list.append(current_number)
            current_number = ""
        else:
            if expression[i] == "**":
                tokens_list.append("**")
                i += 2
            else:
                tokens_list.append(expression[i])
                i += 1

def infix_to_postfix():
        output_postfix = []
        operator_stack = []
        output_postfix.append(tokens_list[0])
        operator_stack.append(tokens_list[1])
        output_postfix.append(tokens_list[2])
        m = 2
        while m < len(tokens_list):
            m += 1
            if power(tokens_list[m]) >= power(operator_stack[-1]):
                operator_stack.append(tokens_list[m])
            else:
                j = 0
                while power(tokens_list[m]) < power(operator_stack[-1]):
                    output_postfix.append(operator_stack.pop())
                    j += 1
                
                operator_stack.append(tokens_list[m])
            m += 1
            output_postfix.append(tokens_list[m])
        
        output_postfix.extend(operator_stack[::-1])
                    
                
        

def power(x):
    if x == "**":
        return 5
    elif x in ["/"]:
        return 4
    elif x in ["*"]:
        return 3
    elif x in ["-"]:
        return 2
    elif x in ["+"]:
        return 1
    else:
        return 0

    
    
    
        

                




def update_output(result):
    text_entry.delete(1.0, tk.END)
    text_entry.insert(1.0, result)

# mainloop
root.mainloop()
