a =['alice','bob','charlie']
try:
    for i in range(4):
        print(a[i])
except:
    print("Something went wrong.")
    #raise an exception
num  = [1,2,3,4,5]
if len(num)>3:
    raise Exception("Too many arguments.")
