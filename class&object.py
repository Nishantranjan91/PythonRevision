# class Business:
#     a = "hello I am attribute"
#     def hello():
#         print("hello I am a method")
# obj = Business()
# print(obj.a)        




class Business:
    a = "hello I am attribute"
    def hello():
        print("hello I am a method")
obj = Business() # obj becomes an object who can access anything
obj2 = Business()
print(obj.a) 
Business.hello()