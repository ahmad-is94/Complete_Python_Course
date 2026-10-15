try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"{a} divided by {b} is {a//b}")
except (ZeroDivisionError, TypeError):
    print("You cannot divide by zero")