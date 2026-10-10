class Account():
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc
    def debit(self,amount):
        self.bal -= amount
        print("rs",amount,'was debit')
        print('total balance ',self.display())

    def credit(self,amount):
        self.bal += amount
        print("rs",amount,'was credit')
        print('total balance ',self.display())

    def display(self):
        return self.bal



a1 =Account(100,100)
print(a1.credit(100))
print(a1.debit(50))
print(a1.display())