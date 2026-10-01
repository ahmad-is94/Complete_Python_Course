'''t = (1,2,3,3,3,3)
t1=t[1:4]
t2 =t[-1]
print(t1)
print(t2)
print(t)
sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")  
print(sampleTuple)
#del sampleTuple
fruits_tuple = ("mango", "orange", "banana", "apple", "papaya") 
print("before changing elements in tuples")
print(fruits_tuple)
# converting the tuple into the list  
list1 =list(fruits_tuple)
list1.append(5)
tuple1 = tuple(list1)
print(tuple1)'''''
#Using Tuple Concatenation
'''t = (1,2,3)
t += (4,)
print(t)
t = (1,2,3)
t = t + (4,)
print(t)
t1 = ("mango", "orange", "banana", "apple", "papaya")  
print(t1)
t2 = (3,)
t1 +=t2
print(t1)'''''
'''t1 = ("mango", "orange", "banana", "apple", "papaya")  
print(t1)
(var_1,var_2,var_3,var_4,var_5) =t1
print(var_1)
print(var_3)
print(var_2)'''
'''fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
print(fruits_tuple)
i = 1
for item in fruits_tuple:
    print(i,"-",item)
    i +=1
    #while loop
    j = 0
    while j < len(fruits_tuple):
        print(j + 1, "-", fruits_tuple[j])
        j +=1'''
'''test_tuple = (12, 23, 35, 76, 84)  
n = 23
m =35
if n in test_tuple:
    print("value is present")
else:
    print("value not found")
if m in test_tuple:
    print(" value is pre")
else:
    print("value is not present")'''
#tuples method
'''T1 = (0, 2, 3, 6, 4, 2, 5, 6, 3, 2, 2, 6, 7, 2, 7, 8, 0, 1, 9, 1)  
t2=T1.count(2)
print(t2)
t3 = T1.index(2)  
print(t3)'''

'''given_tuple = ((4, 5), 1, (4, 5), [4, 5], (2,), 4, 5)    
print(given_tuple)
print(given_tuple.count((4,5)))
print(given_tuple.count([4,5]))'''
 #27 sep 2026
 #sunday


