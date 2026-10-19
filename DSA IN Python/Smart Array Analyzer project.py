
def read_numbers():
    while True:
        try:
            values = input("Enter numbers separated by commas: ")
            numbers = [int(x.strip()) for x in values.split(",")]

            if not numbers:
                print("Array cannot be empty.")
                continue

            return numbers

        except ValueError:
            print("Invalid input. Example: 2, 4, 1, 3, 5")


def analyze_array(numbers):
    total = sum(numbers)

    return {
        "length": len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "sum": total,
        "average": total / len(numbers),
    }


def remove_duplicates_sorted(numbers):
    if not numbers:
        return 0

    i = 0

    for j in range(1, len(numbers)):
        if numbers[j] != numbers[i]:
            i += 1
            numbers[i] = numbers[j]

    return i + 1


def two_sum_pairs_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    pairs = []

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            pairs.append((numbers[left], numbers[right]))

            left_value = numbers[left]
            right_value = numbers[right]

            while left < right and numbers[left] == left_value:
                left += 1

            while left < right and numbers[right] == right_value:
                right -= 1

        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


def max_sliding_window_sum(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    maximum = window_sum

    for i in range(k, len(numbers)):
        window_sum -= numbers[i - k]
        window_sum += numbers[i]
        maximum = max(maximum, window_sum)

    return maximum


def main():
    while True:
        print("===== SMART ARRAY ANALYZER =====")
        print("1. Analyze array")
        print("2. Remove duplicates")
        print("3. Find target-sum pairs")
        print("4. Maximum sliding-window sum")
        print("5. Run all algorithms")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice.")
            continue

        numbers = read_numbers()

        if choice == "1":
            result = analyze_array(numbers)

            for key, value in result.items():
                print(f"{key.title()}: {value}")

            print("Time: O(n), Auxiliary space: O(1)")

        elif choice == "2":
            numbers.sort()
            count = remove_duplicates_sorted(numbers)

            print("Sorted array:", numbers)
            print("Unique count:", count)
            print("Unique elements:", numbers[:count])
            print("Time: O(n) after sorting")

        elif choice == "3":
            numbers.sort()
            target = int(input("Enter target sum: "))

            print("Pairs:", two_sum_pairs_sorted(numbers, target))
            print("Time: O(n) after sorting")

        elif choice == "4":
            k = int(input("Enter window size k: "))
            result = max_sliding_window_sum(numbers, k)

            if result is None:
                print("Invalid k. Choose a value from 1 to", len(numbers))
            else:
                print("Maximum window sum:", result)

            print("Time: O(n), Auxiliary space: O(1)")

        elif choice == "5":
            print("\nArray analysis:", analyze_array(numbers))

            sorted_numbers = sorted(numbers)
            unique_array = sorted_numbers.copy()
            count = remove_duplicates_sorted(unique_array)

            print("Unique elements:", unique_array[:count])

            target = int(input("Enter target sum: "))
            print("Target-sum pairs:",
                  two_sum_pairs_sorted(sorted_numbers, target))

            k = int(input("Enter window size k: "))
            result = max_sliding_window_sum(numbers, k)

            if result is None:
                print("Invalid window size.")
            else:
                print("Maximum window sum:", result)


if __name__ == "__main__":
    main()
