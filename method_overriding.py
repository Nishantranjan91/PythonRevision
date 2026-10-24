# class Animal:
#     name = "lion"
#     def speak(self):
#         print("hello I roar")
# class Human(Animal):
#     name = "Nishant Ranjan"
#     def speak(self):
#         print("hello I tweet")
# obj = Human()
# obj.speak()






# class Animal:
#     name = "sher"
#     def speak(self):
#         print("hello I roar")
# class Human(Animal):
#     name = "Nishant Ranjan"
#     def speak(self):
#         print("hello I tweet")
# obj = Human()
# obj.speak()




#In this example, the parent class Animal has a method called sound(). The child classes Dog and Cat override that method.

class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Calling methods
a.sound()
d.sound()
c.sound()
