def add(x):
    return x+1
def sub(x):
    return x-1
def operator(func, x):
    temp = func(x)
    return temp
print(operator(sub,10))
print(operator(add,20))


def hello():
    def hi():
        print("Hello")
    return hi
new = hello()
new()




# def divide(x,y):
#     print(x/y)
# def outer_div(func):
#     def inner(x,y):
#         if(x<y):
#             x,y = y,x
#            return func(x,y)
# # here, we are returning a function with some passed parameters
#      return inner
# divide1 = outer_div(divide)
# divide1(2,4)