appliances = []


def add_appliance():
    name = input("Enter appliance name: ")

    try:
        watts = float(input("Enter watts: "))
        hours = float(input("Enter hours per day: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    appliance = {
        "name": name,
        "watts": watts,
        "hours": hours,
        "quantity": quantity
    }

    appliances.append(appliance)
    print("Appliance added successfully!")


def view_appliances():
    if len(appliances) == 0:
        print("No appliances added yet.")
        return

    for appliance in appliances:
        print(
            appliance["name"],
            "-",
            appliance["watts"], "W -",
            appliance["hours"], "hours -",
            appliance["quantity"], "quantity"
        )


def daily_usage(appliance):
    usage = (
        appliance["watts"]
        * appliance["hours"]
        * appliance["quantity"]
    ) / 1000

    return usage


def monthly_usage(appliance):
    return daily_usage(appliance) * 30


def show_daily_usage():
    if not appliances:
        print("No appliances added yet.")
        return

    total = 0

    for appliance in appliances:
        usage = daily_usage(appliance)

        print(
            appliance["name"],
            "=", round(usage, 2),
            "units per day"
        )

        total += usage

    print("Total daily usage:", round(total, 2), "units")


def show_monthly_usage():
    if not appliances:
        print("No appliances added yet.")
        return

    total = 0

    for appliance in appliances:
        usage = monthly_usage(appliance)

        print(
            appliance["name"],
            "=",
            round(usage, 2),
            "units per month"
        )

        total += usage

    print("Total monthly usage:", round(total, 2), "units")


def calculate_bill(units):

    if units <= 100:
        bill = units * 10

    elif units <= 300:
        bill = (100 * 10) + ((units - 100) * 15)

    elif units <= 500:
        bill = (
            (100 * 10)
            + (200 * 15)
            + ((units - 300) * 20)
        )

    else:
        bill = (
            (100 * 10)
            + (200 * 15)
            + (200 * 20)
            + ((units - 500) * 30)
        )

    return bill


def show_bill():
    if not appliances:
        print("No appliances added yet.")
        return

    total_units = 0

    for appliance in appliances:
        total_units += monthly_usage(appliance)

    bill = calculate_bill(total_units)

    print("Monthly units:", round(total_units, 2))
    print("Estimated bill: Rs.", round(bill, 2))


def highest_consumer():
    if not appliances:
        print("No appliances added yet.")
        return

    highest = appliances[0]

    for appliance in appliances:
        if monthly_usage(appliance) > monthly_usage(highest):
            highest = appliance

    print("Highest consumer:", highest["name"])
    print(
        "Monthly usage:",
        round(monthly_usage(highest), 2),
        "units"
    )


def main():

    while True:

        print("\n--- Electricity Analyzer ---")
        print("1. Add appliance")
        print("2. View appliances")
        print("3. Daily usage")
        print("4. Monthly usage")
        print("5. Calculate bill")
        print("6. Highest consumer")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_appliance()

        elif choice == "2":
            view_appliances()

        elif choice == "3":
            show_daily_usage()

        elif choice == "4":
            show_monthly_usage()

        elif choice == "5":
            show_bill()

        elif choice == "6":
            highest_consumer()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()