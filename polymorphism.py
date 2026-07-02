# def hello():
#     print("hello I am Nishant Ranjan")

# def hello():
#     print("hello I am aslo a student")
# hello()        



# class Animal:
#     def speak(self):
#         print("hello I roar")
# class Bird:
#     name = "sparrow"
#     def speak(self):
#         print("hello I tweet")
# obj = Animal()
# obj2 = Bird()

# obj.speak()
# obj2.speak()



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