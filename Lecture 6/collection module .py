#Collections Counter Class
'''from collections import Counter
data = ['a', 'b', 'a', 'c', 'b', 'a']
count = Counter(data)
print(count)'''

from collections import defaultdict
from os import remove

dict = defaultdict(int)
A = [1,4,2,3,1,2,5,6,2]
for i in A:
  dict[i] += 1
print(dict)
#Collections ChainMap Class
from collections import ChainMap
dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {'e': 500, 'f': 600}
c = ChainMap(dict1, dict2, dict3)
print(c['a'])
print(c.values())
print(c.keys())
#Collections NamedTuple Class
from collections import namedtuple
Employee = namedtuple('Employee', ['name', 'age', 'ID_number'])
E = Employee('Emil', 21,303)
print(E.name)
print(E.age)
print(E.ID_number)
#Collections Deque Class
'''from collections import deque
q1 = deque(['name','company','empid'])
print(q1)
#Collections UserDict Class
from collections import UserDict
class Dict(UserDict):
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    def __setitem__(self, key, value):
        raise RuntimeError("Setting not allowed")
    def pop(self):
        raise RuntimeError("Pop not allowed")
    def popitem(self):
        raise RuntimeError("Pop not allowed")
d  = Dict({'a' : 1, 'b' : 2, 'c' : 3})
d.popitem()'''
#Collections UserList
from collections import UserList
class List(UserList):
    def remove(self, value):
        raise RuntimeError("Removing not allowed")
    def pop(self):
            raise RuntimeError("Pop not allowed")
L = List([100, 200, 300, 400])
print("Original List")
L.append(100)
print(L)
L.remove()
#Collections UserString Class
from collections import UserString
class string(UserString):
    def append(self, s):
        self.data += s
        def remove(self, s):
            self.data = self.data[:-1]
            str = string("TpointTech")
            print("Original String:", str.data)


