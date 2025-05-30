num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Handle division by zero case.
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    # Handle any unexpected operation input.
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")