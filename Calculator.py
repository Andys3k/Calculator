# Symbol meanings:
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main calculator function
def calculator():
    print("Simple Calculator")

    while True:
        # Taking user input for operation
        operation = input("Enter operation (+, -, *, / or 'exit' to end): ")

        if operation.lower() == 'exit':
            print("Exiting calculator.")
            break

        # Taking user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Performing the selected operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        # Displaying the result
        print(f"Result: {result}")

# Calling the calculator function
calculator()
