
#multiple value return
def add(a,b):
    return a+b,a-b
p=add(1,2)
print(p,p)
def check_eo(a):
    if a%2==0:
     print("even")
    else:
        print("odd")
check_eo(25)
def dhow(a):
    if a==0:#base case is very important in recursion
        return
    print(a)
    dhow(a-1)
    print("end it indicates the call stack")
dhow(5)
def factotrial(n):
        if (n ==1 or n==0):
             return 1
        return n*factotrial(n-1)
print(factotrial(4))