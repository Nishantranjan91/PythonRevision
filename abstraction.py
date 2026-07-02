from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
class   Dog(Animal):
    def sound(self):
        print("hello I make woff sound")

    def hello(self):    
        print("I am a dog and woof")
class cat(Animal):
    def sound(self):
        print("hello I make meow sound")        
obj = Dog()        