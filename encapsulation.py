# class Animal:
#     name = "lion"
#     def speak(self):
#         print("hello I will roar")
# obj = Animal()

# obj.name = "Zebra"
# print(obj.name)



class Animal:
    name = "lion"
    def speak(self):
        print("hello I will roar")
class Human(Animal):
    def say(self):
        print(f"hello my name is {super().name}")
obj = Human()
obj.say()                