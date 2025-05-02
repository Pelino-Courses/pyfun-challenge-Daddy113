def process_operations(*args, **kwargs):
    """
    Processes a sequence of numbers with the specified mathematical operation.

    Parameters:
    *args (float): A sequence of numbers to be processed.
    **kwargs:
        add (bool): If True, performs addition.
        subtract (bool): If True, performs subtraction.
        multiply (bool): If True, performs multiplication.
        divide (bool): If True, performs division.

    Returns:
    float: The result of applying the specified operation in order from left to right.

    Raises:
    ValueError: If no numbers are provided or a non-numeric value is detected.
    ZeroDivisionError: If division by zero is attempted.
    """
    if not args:
        raise ValueError("No numbers provided.")
    for val in args:
        if not isinstance(val, (int, float)):
            raise ValueError(f"Invalid number: {val}")
    result = args[0]
    numbers = args[1:]

    if kwargs.get("add"):
        for num in numbers:
            result += num
    if kwargs.get("subtract"):
        for num in numbers:
            result -= num
    if kwargs.get("multiply"):
        for num in numbers:
            result *= num
    if kwargs.get("divide"):
        for num in numbers:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
    return result


def calculate(*args, **kwargs):
    """
    Safe wrapper for `process_operations` that handles exceptions gracefully.

    Parameters:
    *args (float): Numbers to process.
    **kwargs: Operation flags (add, subtract, multiply, divide).

    Returns:
    float or str: Result of the calculation or error message.
    """
    try:
        return process_operations(*args, **kwargs)
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    """
    Main entry point of the calculator program.

    Prompts the user to:
    - Enter a list of numbers.
    - Select an operation from a menu.
    - Displays the result or appropriate error message.

    Supported operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """
    print("Welcome to the calculator!")

    # Get numbers from user
    numbers_input = input("Enter numbers separated by commas (e.g., 10,5,2): ")
    try:
        numbers = [float(num.strip()) for num in numbers_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        exit()

    # Display operation menu
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4): ").strip()

    # Call calculate with the appropriate keyword
    if choice == "1":
        result = calculate(*numbers, add=True)
    elif choice == "2":
        result = calculate(*numbers, subtract=True)
    elif choice == "3":
        result = calculate(*numbers, multiply=True)
    elif choice == "4":
        result = calculate(*numbers, divide=True)
    else:
        result = "Error: Invalid operation selected."

    print(f"Result: {result}")
