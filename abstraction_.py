#Basic Abstraction using ABC
# from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()