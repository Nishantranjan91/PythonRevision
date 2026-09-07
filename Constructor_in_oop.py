# def Factory(material,zips,pockets):
#     pass
# Factory(material=22,zips=22,pockets=22)
# print(Factory)





# class Student:
#     def __init__(self):
#         print("Constructor called")


# s1 = Student()




# Constructor ke through object ko data de sakte hain
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rahul", 21)
s1.display()




# class Factory:
#     def __init__(self):
#         print("It is raining cats and dogs")
# Factory()        