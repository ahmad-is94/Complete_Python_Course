# def insertion_sort(list1):
#     # Outer loop to traverse through 1 to len(list1)
#     for i in range(1, len(list1)):
#
#         value = list1[i]
#
#         # Move elements of list1[0..i-1], that are
#         # greater than value, to one position ahead
#         # of their current position
#         j = i - 1
#         while j >= 0 and value < list1[j]:
#             list1[j + 1] = list1[j]
#             j -= 1
#         list1[j + 1] = value
#     return list1
#     # Driver code to test above
#
#
# list1 = [10, 5, 13, 8, 2]
# print("The unsorted list is:", list1)
#
# print("The sorted list1 is:", insertion_sort(list1))


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "({},{})".format(self.a, self.b)


def insertion_sort(list1, compare_function):
    for i in range(1, len(list1)):
        Value = list1[i]
        Position = i

        while Position > 0 and compare_function(list1[Position - 1], Value):
            list1[Position] = list1[Position - 1]
            PositionPosition = Position - 1

        list1[Position] = Value


U = Point(2, 3)
V = Point(4, 4)
X = Point(3, 1)
Y = Point(8, 0)
Z = Point(5, 2)

list1 = [U, V, X, Y, Z]

# Sort by x-coordinate (ascending)
insertion_sort(list1, lambda x, y: x.a > y.a)

print("The points are in the sorted order")
for point in list1:
    print(point)  