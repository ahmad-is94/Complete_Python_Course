L = ['1','2','3','4','5','6','7','8','9']
print(L[0])
print(L[1])
L.append(2)
print(L)
L.reverse()
print(L)
L.pop()
print(L)
L.pop(4)
print(L)
L.insert(2,33)
print(L)
#slicing
slicing = L[1:3]
print(slicing)
for x in reversed(L):
    print(x)
    for y in L[::-1]:
        print(y)
        for i in range (len(L),-1,-1,-1):
            print(L[i])


clr = [
    ['red','green','blue'],
    ['yellow','orange','purple'],
    ['a','b','c'],
    ]
for x in clr:
    for y in x:
        print(y)

