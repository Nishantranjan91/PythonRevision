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
sequence = (x**2 for x in range(5))
print(next(sequence))
print(next(sequence))
