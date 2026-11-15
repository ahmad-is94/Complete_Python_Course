MIN_MERGE = 32


def calcMinRun(n):
    """It returns the minimum run length
     (between 23 and 64) such that dividing
      the array length by this value results
      in a number less than or equal to a power of two.
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# this sorts the array for left-to-right index
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        # The merge function merges the sorted runs


def merge(arr, l, m, r):
    # here, the array is divided into two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # merging two arrays into one after comparing
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

        # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

        # Copy remaining element of the right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

    # Iterative Timsort function to sort the array


def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:

        # Pick the starting point of the left subarray. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase the left by 2*size
        for left in range(0, n, 2 * size):

            # Find the ending point of the left sub-array
            # mid+1 is the starting point of the right subarray
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

    # Driver program to test the above function


if __name__ == "__main__":
    array = [18, 2, 1, 12, 5, 3, 8, 11, 7]

    print("Given Array is:")
    print(array)

    # Function Call
    timSort(array)

    print("After Sorting, the Array is:")
    print(array)