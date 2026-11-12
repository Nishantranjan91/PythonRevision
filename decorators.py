# def say_hello():
#     print("hello")
# say_hello()    




# def my_decorator(func):
#     def wrapper():
#         print("hello I will print before")
#         func()  
#         print("hello I will print after")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello")
# say_hello()






# def decorate(func):
#     def wrapper(a,b):
#         print("your two numbers additions is: ")
#         func(a,b)
#         print("Thank you for using us")
#     return wrapper    
    



# @decorate
# def addition(a,b):
#     print(a+b)


# Simple Decorator Function
def my_decorator(func):

    def wrapper():
        print("Before calling the function")

        func()

        print("After calling the function")

    return wrapper


@my_decorator
def hello():
    print("Hello Nishant!")


hello()