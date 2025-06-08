def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

if __name__ == "__main__":
    print("--- Testing perform_operation function directly ---")

    print(f"5 + 3 = {perform_operation(5, 3, 'add')}")
    print(f"10 - 4 = {perform_operation(10, 4, 'subtract')}")
    print(f"7 * 2 = {perform_operation(7, 2, 'multiply')}")
    print(f"9 / 3 = {perform_operation(9, 3, 'divide')}")
    print(f"5 / 0 = {perform_operation(5, 0, 'divide')}")
    print(f"10 + 2 (invalid op) = {perform_operation(10, 2, 'power')}")
    print(f"2.5 * 4.0 = {perform_operation(2.5, 4.0, 'multiply')}")