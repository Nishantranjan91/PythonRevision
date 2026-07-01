class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

        
    def info(self):
        print("this is a method")
    @classmethod
    def clmethod(cls):
        print(f"{cls.gender} is your gender")
    @staticmethod    
    def hello():
        print("hello I am static method")    
obj = Animal("Lion",12)        
obj.info()
obj.clmethod()
obj.hello()