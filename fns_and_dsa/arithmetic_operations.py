def perform_operation(num1, num2, operation):
    if "add" in operation:
        return num1 + num2
    elif "subtract" in operation:
        return num1 - num2
    elif "multiply" in operation:
        return num1 * num2
    elif "divide" in operation:
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Enter a valid operation."