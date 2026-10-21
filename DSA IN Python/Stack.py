def c():
    print("Hello World")
def b():
        c()
def a():
            b()


a()

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print("stack item",stack[-1])
print(stack.pop())
print(stack)
#check if the stack is empty or not
print(len(stack)==0)



#Stack by using class method
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
            if self.is_empty():
                return None
                return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items[::-1])

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("values ")
s.display()
print(s.peek())
s.pop()
print (len(s) == 0)



