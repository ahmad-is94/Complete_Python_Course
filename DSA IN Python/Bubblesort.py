def sort_numbers(data):
    size = len(data)
    for i in range(size):
        for j in range(0, size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
# Example usage
numbers = [45, 12, 78, 3, 56, 21, 9]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)


def flagged_bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = flagged_bubble_sort(arr)
print(sorted_arr)