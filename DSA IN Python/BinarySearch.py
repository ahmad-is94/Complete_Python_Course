def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")


def binary_search(list1, low, high, n):
    # Check base case for the recursive function
    if low <= high:

        mid = (low + high) // 2

        # If element is available at the middle itself then return the its index
        if list1[mid] == n:
            return mid

            # If the element is smaller than mid value, then search moves
        # left sublist1
        elif list1[mid] > n:
            return binary_search(list1, low, mid - 1, n)

            # Else the search moves to the right sublist1
        else:
            return binary_search(list1, mid + 1, high, n)

    else:
        # Element is not available in the list1
        return -1

    # Test list1ay


list1 = [12, 24, 32, 39, 45, 50, 54]
n = 32

# Function call
res = binary_search(list1, 0, len(list1) - 1, n)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in list1")