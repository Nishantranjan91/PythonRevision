# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 

        
#     def info(self):
#         print("this is a method")
#     @classmethod
#     def clmethod(cls):
#         print(f"{cls.gender} is your gender")
#     @staticmethod    
#     def hello():
#         print("hello I am static method")    
# obj = Animal("Lion",12)        
# obj.info()
# obj.clmethod()
# obj.hello()




class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

    @classmethod
    def college(cls):
        print("This student belongs to ABC College")

    @staticmethod
    def hello():
        print("Hello I am a static method")


obj = Student("Rahul", 20)

obj.info()
obj.college()
obj.hello()