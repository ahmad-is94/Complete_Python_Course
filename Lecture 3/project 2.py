# Monthly Expense Tracker

Budget = float(input("Enter your monthly budget: "))

Expenses = []

# Taking expenses
while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    Expenses.append([category, amount])
    choice = input("Do you need to add another expense? (yes/no): ")
    if choice.lower() == "no":
        break


# Calculate total
total = 0
for E in Expenses:
    total = total + E[1]
# Calculate average
average = total / len(Expenses)
# Highest and lowest expense
amounts = []
for E in Expenses:
    amounts.append(E[1])
highest = max(amounts)
lowest = min(amounts)
# Display result
print("monthly expenses : ")
print("Monthly Budget:", Budget)
print("Total Expenses:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)

# Budget checking
if total > Budget:
    print("You are exceeding your budget!")
else:
    print("You are within your budget.")

# Display all expenses
print(" All Expenses ")
for E in Expenses:
    print("Category:", E[0], "| Amount:", E[1])
