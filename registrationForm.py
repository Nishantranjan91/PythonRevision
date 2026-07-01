class Registration:
    def __init__(self,name,age,number,bloodgroup):
        self.age = age  
        self.name = name 
        self.number = number
        self.bloodgroup = bloodgroup
    def info(self):
        print(f"your name is {self.name}\n your age is {self.age}\n your number is {self.number}\n your bloodgroup is {self.bloodgroup}")   
student1 = Registration("Nishant Ranjan",27,1111111111,"B+")     
student2 = Registration("Santosh Kumar",24,1111112111,"A+")  
student3 = Registration("Vivek Raj",23,1111114111,"A-")   

student1.info()
student2.info()
student3.info()