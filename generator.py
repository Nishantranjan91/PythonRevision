# def my_generator():
#     for i in range(5):
#         return i
# print(my_generator())    




# def my_generator():
#     for i in range(5):
#         print(i)
# my_generator()




# def my_generator():
#     for i in range(5):
#         yield i
# gen = my_generator()
# print(next(gen))      




# def my_generator():
#     for i in range(5):
#         yield i
# gen = my_generator()
# print(next(gen))      
# print(next(gen))
# print(list(gen)) 





#generator comprehension
# sequence = (x**2 for x in range(5))
# print(next(sequence))
# print(next(sequence))




#Generator to print numbers from 1 to 5
def my_generator():
    for i in range(1, 6):
        yield i


# Calling generator
result = my_generator()

for num in result:
    print(num)