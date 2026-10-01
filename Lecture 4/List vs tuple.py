'''Mutability Test: Lists vs Tuples
The main difference between a list and a tuple is mutability.
 A list is mutable, which means its elements can be changed, added, or removed after it is created.
On the other hand, a tuple is immutable, which means its elements cannot be changed after creation.
 Any attempt to modify a tuple will result in an error.'''
# Modifying a list  
'''lst = [14, 23, 39]  
print("Given List:", lst)  
lst[0] = 17  
print("Modified List:", lst)  
  
print()  
# Modifying a tuple (Raises an error)  
tpl = (14, 23, 39)  
print("Given Tuple:", tpl)  
tpl[0] = 17  # TypeError: 'tuple' object does not support item assignment  '''
'''Performance and Memory Comparison: Lists vs Tuples
  This is because lists need extra memory to allow changes like adding or removing elements, while tuples are fixed and stored in a more optimized way.                                                                                                                         '''
'''Tuples are generally faster and use less memory than lists.'''
import sys  
  
lst = [19, 24, 3, 54, 25]  
tpl = (19, 24, 3, 54, 25)  
  
print(sys.getsizeof(lst))  # More memory usage  
print(sys.getsizeof(tpl))  # Less memory usage  