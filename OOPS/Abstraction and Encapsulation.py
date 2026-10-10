#hiding the unnecessary implementation detailed of class
class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.race =False
    def get_start(self):
        self.acc = True
        self.clutch = True
        print("car is started")
c1 = Car()
c1.get_start()