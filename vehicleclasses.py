from abc import ABC, abstractmethod
class Vehicle(ABC):
    def speed(self):
        pass
    def mileage(self):
        pass
    def price(self):
        pass
class BMW(Vehicle):
    def speed(self):
        print("150kmph")
    def mileage(self):
        print("300 km")
    def price(self):
        print("$200,000")
class Ferrari(Vehicle):
    def speed(self):
        print("200 kmph")
    def mileage(self):
        print("350 km")
    def price(self):
        print("$500,000")

obj1 = BMW()
obj2 = Ferrari()
obj1.speed()
obj2.speed()
obj1.mileage()
obj2.mileage()
obj1.price()
obj2.price()