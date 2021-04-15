# class Car:  #parent class
#     def __init__(self, name, mileage):
#         self._name = name  #protected variable
#         self.mileage = mileage

#     def description(self):
#         return "The {name} car gives the mileage of {mileage}km/l".format(
#             name=self._name, mileage=self.mileage)

# class Audi:
#     def description(self):
#         print("This the description function of class AUDI.")

# class BMW:
#     def description(self):
#         print("This the description function of class BMW.")

# # return "The {name} runs at the maximum speed of {speed}km/hr".format(name = "shubham", speed = 100)

# audi = Audi()
# bmw = BMW()
# for car in (audi, bmw):
#     car.description()

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def price(self, x):
        pass
