str_1 = "hi my name is ahmad ali"
print(str_1)
print(str_1[0])
#slicing
print(str_1[1:3])
#concatenation
str= "a"+"b"
print(str)
a = "ahmad ali"
del a

#upper and lower method 
#f string 
#update a string 
name = " ali"
age = 12
city = "multan"
print(f'{name} is a {age} years old boy living in {city}.')  
#format method
name = "ali"
age  = 20
frmt = "My name is {} and i am {} years old .".format(name,age)
print(frmt)
#methods of string
a = "my name is Ali"
print (a.swapcase())
#Boolean operator and or not 
a = [12,2,3,3]
b = a
c = b
print (b is a)
print(c is a)
#in operatoe it checks a value is present inside ancontainer like string tuple lists it return ture and false
a = [12,2,2,2]
print(17 in a)