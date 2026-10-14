# Encapsulation means keeping data and methods together inside a class and controlling access to the data.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student("Nishant", 85)

print(s1.name)
print(s1.get_marks())