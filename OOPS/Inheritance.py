# class Car:
#     color = "red"
#     @staticmethod
#     def start():
#         return "My car class start"
#     @staticmethod
#     def stop():
#         return "My car class stop"
# class toyotacar(Car):
#         def __init__(self,name):
#             self.name = name
# class toyotacar2(toyotacar):
#     def __init__(self,brand):
#         self.brand = brand
#
#
#
# c1 = toyotacar2('fortuner')
# print(c1.color)
# print(c1.start())
# print(c1.stop())
# multiple inheritance
# class A:
#      var1 = "wlcome to class a"
# class B:
#     var2 = "wlcome to class B"
# class C(A,B):
#     var3 = "wlcome to C"
#
# c1 = C()
# print(c1.var1)
# print(c1.var2)
#
# class Car:
#     def __init__(self,type ):
#         self.type = type
#     @staticmethod
#     def start():
#         return "Car is starting"
#     @staticmethod
#     def stop():
#             return "Car is stopping"
# class toyota(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()
#
# c1 = toyota("toyota",'petrol')
# print(c1.name)
# print(c1.type)
# print(c1.start())
# print(c1.stop())