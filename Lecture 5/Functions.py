def welcome(name):
    print(f"Hello {name}!")

welcome('Ahmad')

def calculate_avg(a,b,c):
    sum = a + b  + c
    avg = sum/3
    print(f"The average is: {avg}")
    return avg
calculate_avg(1,2,3)
def calculate_pro(a=1,b=2,c=4):
    print(f"The product is: {a*b*c}")
    return a*b*c
calculate_pro(1,2,3)
cities =['karachi','islamabad','lahore']
name =['ahmad','ali','sohrani']
def printlen(list):
    print(len(list))
    return len(list)
printlen(cities)
printlen(name)
def print_len(list):
    for item in list:
        print(item,end="")
        print_len(cities)
        print()
        print_len(name)

n = 5
fact = 1
for i in range(1,n+1):
        fact *= i
        print(fact)

def calc_fact(n):
     fact = 1
     for i in range(1,n+1):
         fact *= i
     print(fact)
calc_fact(9)

def convertor(USD_value):
    pkr_rs =USD_value*287
    print(USD_value,pkr_rs)
convertor(10)