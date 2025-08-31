def calculator(a, b, operation):
    if operation == '+': return a + b
    elif operation == '-': return a - b
    elif operation == '*': return a * b
    elif operation == '/': return a / b if b != 0 else "Division by zero error"
    else: return "Invalid operator"
 
print(calculator(10, 5, '+'))
print(calculator(10, 5, '/'))