#A new  list formation from xisting list (modules sections of python)
numlist = [4, 32, 6, 76, 12, 37, 52]
square = [sol ** 2 for sol in numlist]
print(square)
#Difference between For Loop and List Comprehension
numlist1 = [4, 32, 6, 76, 12, 37, 52]
S = []
for sol in numlist1:
     S.append(sol)
print(S)
#Conditional Statements in List Comprehension
car = ['tata', 'honda', 'toyota', 'hyundai', 'skoda', 'suzuki', 'mahindra', 'BMW', 'Mercedes']
new_list = [x for x in car if x  in car]
print(new_list)
ar = ['tata', 'honda', 'toyota', 'hyundai', 'skoda','suzuki', 'mahindra', 'BMW', 'Mercedes']
indain_car =['mahindra','suzuki']
new_list1 = [x for x in ar if x not in indain_car]
print(new_list1)
#List Comprehension with String]
name  = 'ahmad ali'
vowels = "aeiou"
list = [lette for lette in name if lette in vowels]
print(list)
#
#Using range() with List Comprehension
num = [x for x in range(10)]
print(num)
#Creating a List using Nested Loops
cubes = [(i,i**3) for i in range(10)]
print(cubes)
#Flattening a List of Lists
lists = [[1,2,3],[4,5,6],[7,8,9]]
result = [x for y in lists  for x in y]
print(result)