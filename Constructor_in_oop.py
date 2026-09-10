# def Factory(material,zips,pockets):
#     pass
# Factory(material=22,zips=22,pockets=22)
# print(Factory)





# class Student:
#     def __init__(self):
#         print("Constructor called")


# s1 = Student()




# Constructor ke through object ko data de sakte hain

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Rahul", 21)
# s1.display()





# Ek hi class se multiple objects bana sakte hain
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(self.name, self.marks)


# s1 = Student("Rahul", 85)
# s2 = Student("Nidhi", 90)
# s3 = Student("Aman", 78)

# s1.display()
# s2.display()
# s3.display()



# Ye interview mein bhi common example hai.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary.p

#     def display(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)


# e1 = Employee("Amit", 50000)
# e1.display()





# Agar user value provide na kare, to default value use ho sakti hai.
# class Student:
#     def __init__(self, name="Unknown", age=18):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student()
# s2 = Student("Rahul", 21)

# s1.display()
# s2.display()




# Constructor mein values lekar calculation bhi kar sakte hain
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth


# r1 = Rectangle(10, 5)

# print("Area =", r1.area())



# class Factory:
#     def __init__(self):
#         print("It is raining cats and dogs")
# Factory()        




# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
# obj = Factory("Leather",3,3)        
# print(obj.material)




class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    def showdetails(self):
        print(self.material,self.pockets,self.zips)    
reebok = Factory("Leather",3,3)  
campus = Factory("nylon",2,2)      
campus.showdetails()