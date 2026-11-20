from array import *

marks = array('i', [85, 90, 78, 92, 88])

for m in marks:
    print(m)



#Accessing array elements
import array as arr
a = arr.array('i', [2, 4, 5, 6])
print("First element is:", a[0])
print("Second element is:", a[1])
print("Third element is:", a[2])
print("Fourth element is:", a[3])
print("Last element is:", a[-1])
print("Second last element is:", a[-2])
print("Third last element is:", a[-3])
print("Fourth last element is:", a[-4])
print(a[0], a[1], a[2], a[3], a[-1],a[-2],a[-3],a[-4])



#Changing or Adding Elements
import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing the first element 1 to the value 0.
numbers[0] = 0
print(numbers)  # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing the last element 10 to the value 8.
numbers[5] = 8
print(numbers)  # Output: array('i', [0, 2, 3, 5, 7, 10])

# replace the value of 3rd to 5th element by 4, 6 and 8
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)  # Output: array('i', [0, 2, 4, 6, 8, 10])


#Deleting Elements from an Array
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])
del number[2]                           # removing third element
print(number)                           # Output: array('i', [1, 2, 3, 4])

#Finding Length of an Array
from array import *

numbers = array('i', [10, 20, 30, 40, 50])

length = len(numbers)
print("Length of the array:", length)


