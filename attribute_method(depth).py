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




# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"My name is {self.name} and my age is {self.age}")

#     @classmethod
#     def college(cls):
#         print("This student belongs to ABC College")

#     @staticmethod
#     def hello():
#         print("Hello I am a static method")


# obj = Student("Rahul", 20)

# obj.info()
# obj.college()
# obj.hello()





class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee name is {self.name}")
        print(f"Employee salary is {self.salary}")

    @classmethod
    def company(cls):
        print("Employee works in ABC Company")

    @staticmethod
    def welcome():
        print("Welcome to our company")


obj = Employee("Amit", 50000)

obj.show()
obj.company()
obj.welcome()