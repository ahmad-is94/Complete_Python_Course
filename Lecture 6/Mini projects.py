
import statistics
import random

expenses = []

while True:
    print("1--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total and Average")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "id": random.randint(1000, 9999),
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        for expense in expenses:
            print(expense)

    elif choice == "3":
        if expenses:
            amounts = [e["amount"] for e in expenses]

            print("Total:", sum(amounts))
            print("Average:", statistics.mean(amounts))
        else:
            print("No expenses recorded yet.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
