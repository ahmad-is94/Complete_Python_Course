'''#sets
s = {1,2,3,3,4}
print(s)
#set method and by curly brackets
list =[1,2,3]
set1 =set(list)
print(set1)

empty_set = set()
print(empty_set)
#we can access the elements of set by using loop statement
set2 = {"a",3,32.33}
print(set2)
##  print(e)
set2.add("b")
set2.update([1,2,3],('a',))
print(set2)
subjects = {'physics', 'chemistry', 'english', 'biology', 'computer', 'maths'}  
print("Given Set:", subjects)  
subjects.remove('physics')
print(subjects)
subjects.discard('ict')
print(subjects)
subjects.pop()
print(subjects)
subjects.clear()
print(subjects)'''
#UNION SETS
a = {1,2,3}
b ={2,5,6}
print(a | b)
print(a.union(b))
#intersection
print(a.intersection(b))
print(a & b)
print(a - b)
print(a.difference(b))


sset = {i**2 for i in range(6)}
print(sset)
set3 = frozenset([1,2,3,4])
print(set3)
print(type(set3))