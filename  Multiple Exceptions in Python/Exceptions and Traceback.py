try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if second == 0:
        raise ZeroDivisionError

    result = first / second
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("You cannot divide by zero")

except Exception as e:
    print("Unexpected error:", e)