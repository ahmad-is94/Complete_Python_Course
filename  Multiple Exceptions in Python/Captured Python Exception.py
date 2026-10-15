# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(f"{a} divided by {b} is {a//b}")
# except (ZeroDivisionError,value):
#     print("You cannot divide by zero")

from operator import mul, truediv


def calculate(operator, operand1, operand2):
    return operator(operand1, operand2)


try:
    first = float(input("Enter your first number: "))
    second = float(input("Enter your second number: "))
    operation = input("Enter either * for multiplication or / for division: ")

    if operation == "*":
        answer = calculate(mul, first, second)
    elif operation == "/":
        if second == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        answer = calculate(truediv, first, second)
    else:
        raise ValueError("Unsupported operation")

except (ValueError, ZeroDivisionError, RuntimeError) as error:
    print(f"An error occurred: {error}")
    if isinstance(error, ValueError):
        print("Make sure you entered valid numbers.")
    elif isinstance(error, ZeroDivisionError):
        print("You can't divide by zero.")
    elif isinstance(error, RuntimeError):
        print("Unsupported operation.")
else:
    print(f"{first} {operation} {second} = {answer}")