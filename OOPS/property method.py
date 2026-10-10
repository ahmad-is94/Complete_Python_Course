class Student:
    def __init__(self, phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.percentage =str((self.phy + self.chem + self.bio) / 3) + '%'

s1 = Student(123,34,56)
print(s1.percentage)
s1.bio = 59
print(s1.bio)
print(s1.percentage)








class Student:
    def __init__(self, phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.percentage =str((self.phy + self.chem + self.bio) / 3) + '%'
    def p(self):
        self.percentage = str((self.phy + self.chem + self.bio) / 3) + '%'

s1 = Student(123,34,56)
print(s1.percentage)
s1.bio = 59
print(s1.bio)
s1.p()
print(s1.percentage)









#property method usage

class Student:
    def __init__(self, phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def percentage(self):
            return str((self.phy + self.chem + self.bio) / 3) + '%'
s1 = Student(123,67,56)
print(s1.percentage)
s1.bio = 45
print(s1.percentage)
print(s1.bio)



