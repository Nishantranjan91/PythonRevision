class Animal:
    def __init__(self,name,age):
            self.name = name
            self.age = age
    def info(self):
          print(f"your name is {self.name} and your age is {self.age}")        
obj1 = Animal("Lion",12)

class Human(Animal):
        pass

obj = Animal("Lion",12)
obj2 = ("Nishant",27)
      