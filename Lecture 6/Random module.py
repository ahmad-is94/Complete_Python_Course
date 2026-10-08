#Usage of Seed Values
import random
random.seed(1)
print(random.random())
print(random.random())
#adding more numbers
random.seed(7)
print(random.random())
#$ Using the randint() function
p = random.randint(1, 100)
print(p)
print(random.random())
print(random.random())
#using rand eange method
import random
#using the randrange()function
n1 = random.randrange(1, 15, 2)
#printing the random value
print (n1)
#Generate a Random Float between 0 and 1
p1  =random.random()
print (p1)
#Randomly Select from List, String, and Tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#printing random elements from the list
print(random.choice(my_list))
#declaring a string
my_string = "Tpoint"
#printing random elements from the string
print(random.choice(my_string))
#declaring a tuple
my_tuple = (2, 0, 1, 9)
#printing random elements from the tuple
print(random.choice(my_tuple))