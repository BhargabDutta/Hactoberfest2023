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
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    # Display the menu options to the user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    # User input, converted to lowercase for case insensitivity
    user_input = input(": ").lower()

    # Check if the user wants to exit
    if user_input == "exit":
        break

    # Check if the user's input is a valid operation
    if user_input in ("add", "subtract", "multiply", "divide"):
        try:
            # Get the numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Perform the selected operation and provide feedback
        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
    else:
        print("Invalid input. Please enter a valid operation.")

# End of the program
