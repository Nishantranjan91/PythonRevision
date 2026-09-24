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
from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass


class BMW(Car):

    def start(self):
        print("BMW starts with a button")


class Tesla(Car):

    def start(self):
        print("Tesla starts automatically")


car1 = BMW()
car1.start()

car2 = Tesla()
car2.start()