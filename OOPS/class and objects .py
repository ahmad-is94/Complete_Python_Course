class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0

        for val in self.marks:
            sum += val
            print("Hi",self.name,"avg marks:",sum/len(self.marks))

s1=Student("James",[10,20,30,40])
s1.get_avg()

s1.name="ALI"
s1.get_avg()

