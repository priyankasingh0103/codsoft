import tkinter as tk

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def mod(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero!"

def perform_operation():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    choice = choice_var.get()
    
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = sub(num1, num2)
    elif choice == '3':
        result = mul(num1, num2)
    elif choice == '4':
        result = div(num1, num2)
    elif choice == '5':
        result = mod(num1, num2)
    else:
        result = 'Invalid input'
    
    result_label.config(text="Result: " + str(result))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

operation_label = tk.Label(root, text="Select operation:")
operation_label.pack()

# Create radio buttons for operation choice
choice_var = tk.StringVar(root, '1')
tk.Radiobutton(root, text="Addition", variable=choice_var, value='1').pack()
tk.Radiobutton(root, text="Subtraction", variable=choice_var, value='2').pack()
tk.Radiobutton(root, text="Multiplication", variable=choice_var, value='3').pack()
tk.Radiobutton(root, text="Division", variable=choice_var, value='4').pack()
tk.Radiobutton(root, text="Modulus", variable=choice_var, value='5').pack()

# Create button to perform operation
calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
calculate_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start GUI event loop
root.mainloop()
