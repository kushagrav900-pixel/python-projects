import re

# Operator precedence mapping
PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "**": 3
}

def tokenize(expression):
    # Splits numbers, **, and single-char operators, ignoring whitespace
    return re.findall(r'\d+\.?\d*|\*\*|[+\-*/()]', expression)

def infix_to_postfix(tokens):
    output = []
    stack = []
    
    for token in tokens:
        if re.match(r'^\d+\.?\d*$', token):  # Check if number
            output.append(token)
        elif token in PRECEDENCE:
            # Pop operators with higher or equal precedence
            while stack and stack[-1] in PRECEDENCE and PRECEDENCE[stack[-1]] >= PRECEDENCE[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop() # Remove '('
                
    while stack:
        output.append(stack.pop())
        
    return output

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if re.match(r'^\d+\.?\d*$', token):
            stack.append(float(token))
        elif token in PRECEDENCE:
            if len(stack) < 2:
                raise ValueError("Invalid expression (insufficient operands)")
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "**":
                stack.append(a ** b)
                
    if len(stack) != 1:
        raise ValueError("Invalid expression (leftover operands)")
    return stack[0]

def main():
    print("=== Simple Postfix Calculator (CLI) ===")
    print("Enter infix expression (e.g. 3 + 4 * 2 / ( 1 - 5 ) ) or 'q' to quit:")
    while True:
        try:
            expr = input("> ")
            if expr.strip().lower() == 'q':
                break
            if not expr.strip():
                continue
                
            tokens = tokenize(expr)
            postfix = infix_to_postfix(tokens)
            result = evaluate_postfix(postfix)
            
            print(f"Tokens:  {tokens}")
            print(f"Postfix: {' '.join(postfix)}")
            print(f"Result:  {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
