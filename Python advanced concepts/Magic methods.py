#Python __init__() Method

class methods():
    def __init__(self, *args):
        print("Now called __init__ magic method, after tha initialised parameters")
        self.name = args[0]
        self.std = args[1]
        self.marks = args[2]


Student = methods("Ali", 11, 98)
print(Student)
print(f"Name, standard, and marks of the student is: \n", Student.name, Student.std,  Student.marks)
#
#Python __new__() Method
class Method(object):
    def __new__(cls):
        print("Creating an instance by __new__ method")
        return super(Method, cls).__new__(cls)
        # Calling the init method

    def __init__(self):
        print("Init method is called here")


Method()
#Python __add__ Method
class Method:
    def __init__(self, argument):
        self.attribute = argument

    # Creating a second class


class Method_2:
    def __init__(self, argument):
        self.attribute = argument
    # creating the instances


instance_1 = Method(" Attribute")
print(instance_1.attribute)
instance_2 = Method_2(" 27")
print(instance_2.attribute)

# Adding two attributes of the instances
print(instance_2.attribute + instance_1.attribute)
#Python __repr__ Method
class Method:
    # Initializing the attributes of the class
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # Defining the __repr__ method

    def __repr__(self):
        return f"""Following are the values of the attributes of the class Method: 
x = {self.x} 
y = {self.y} 
z = {self.z}"""
    # Creating an object


instance = Method(4, 6, 2)

# Printing the object
print(instance)


#Python __contains__ Method
class Method:
    # Calling the __init__ method and initializing the attributes
    def __init__(self, attribute):
        self.attribute = attribute

        # Calling the __contains__ method

    def __contains__(self, attribute):
        return attribute in self.attribute
    # Creating an instance of the class


instance = Method([4, 6, 8, 9, 1, 6])

# Checking if a value is present in the container attribute
print("4 is contained in ""attribute"": ", 4 in instance)
print("5 is contained in ""attribute"": ", 5 in instance)


#Python __call__ Method

# Creating a class
class Method:
    # Calling the __init__ method and initializing the attributes
    def __init__(self, a):
        self.a = a
        # Calling the __call__ method to multiply a number to the attribute value

    def __call__(self, number):
        return self.a * number

    # Creating an instance and proving the value to the attribute a


instance = Method(7)
print(instance.a)  # Printing the value of the attribute a
# Calling the instance while passing a value which will call the __call__ method
print(instance(5))

