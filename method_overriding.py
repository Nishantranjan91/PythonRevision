class Animal:
    name = "lion"
    def speak(self):
        print("hello I roar")
class Human(Animal):
    name = "Nishant Ranjan"
    def speak(self):
        print("hello I tweet")
obj = Human()
obj.speak()