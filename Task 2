def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

while True:
    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display operation options
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user's choice of operation
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid input. Please enter a valid operation (1/2/3/4).")
        continue

    # Display the result
    print("Result:", result)

    # Ask the user if they want to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
