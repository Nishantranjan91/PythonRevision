#Basic Abstraction using ABC
# from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# dog = Dog()
# dog.sound()




# Abstraction with Car
# from abc import ABC, abstractmethod

# class Car(ABC):

#     @abstractmethod
#     def start(self):
#         pass


# class BMW(Car):

#     def start(self):
#         print("BMW starts with a button")


# class Tesla(Car):

#     def start(self):
#         print("Tesla starts automatically")


# car1 = BMW()
# car1.start()

# car2 = Tesla()
# car2.start()




# Abstraction with Payment System
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


payment1 = CreditCard()
payment1.pay(1000)

payment2 = UPI()
payment2.pay(500)