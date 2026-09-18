class Animal: # parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"your name is {self.name} and your age is {self.age}")    





class human(Animal): # child class
    def __init__(self, name, age, number, group):
        super().__init__(name, age)
        self.number = number
        self.group = group



obj = Animal("Lion",12)
obj2 = human("Nishant Ranjan",27,1234, "B+")
obj2.info()