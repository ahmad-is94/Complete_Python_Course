#Everything in Python is an object.
#  From this aspect, we can consider that data types are the classes, and the variables are instances of these classes.
# python program to show how to declare integers in Python  
  
# initializing some variables with integers  
var_1 = 16   
var_2 = -21   
var_3 = 0   
  
# printing the types of initialized variables  
print( type(var_1))  
print( type(var_2))  
print( type(var_3))

var_1 = 16.44  
var_2 = -22.22 
var_3 = 12.3  
var_4 = 1.6e4
  
# printing the types of initialized variables  
print( type(var_1))  
print( type(var_2))  
print( type(var_3))  
print( type(var_4))  
#complex numbers 
var_1 = 3 + 5j  
var_2 = -3.4 + 2.8j  
var_3 = -5 - 1.9j  
var_4 = -6 + 0j  
print( type(var_1))  
print( type(var_2))  
print( type(var_3))  
print( type(var_4))  
#Sequence Data Types
list1 = [1,2,3,"ahmad ",1.7e3,33.3333]
print(type(list1))
# Tuples (tuple)
tuple =(1, 0.5, 'hello', 1+5j, 1.7e2, -12, 'welcome')
print(tuple)
#str
str_2 = "my name is ahmad ali"
print(str_2)
#range
# creating a range  
r = range(3, 26, 3)  
# printing the results  
print("Range:", r) # printing range 
# printing range as a list 
print( list(r))

#set datatypes
set_1 = {"mango","orange"}
st_2  = set(["ginger", "lemon"])  
  
print(set_1)
print(st_2)
#frozenset
list_1 = ["berries", "orange", "mango", "apple"] 
f_1 = frozenset(list_1)
print(f_1)
#mapping datatypes
dict_1 = {
    "name" : "ahmad ali ",
    "marks":  90
}
print(dict_1)
#boolian datatyps
a  = True 
b = False
print (a,b)
#bytes datatypes
obj_1 = bytes([78,88,44])
print(obj_1)
#bytearray
a  = bytearray([12,3,4,5,66])
print(a)