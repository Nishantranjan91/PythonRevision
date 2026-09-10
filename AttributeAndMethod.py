class Animal:
    gender = "Male" # class attribute
    name = "lion"
    def __init__(self,name,age):
        self.name = name #instance attribute
        self.age = age
    def info():
        print("this is a method")    
    def speak():
        print("Lion is roaring")
obj = Animal("lion",12)        
obj.info()