# a = [1,2,3,4,5]
# l = []
# for i in a:
#     l.append(i**2)
# print(l)    




# a = [1,2,3,4,5]
# l = map(lambda x :x**2,a)
# print(list(l))




# def square(x):
#     return x**2
# a = [1,2,3,4,5]
# l = map(square,a)
# print(list(l))





#filter
# a = [1,2,3,4,5,6,8,9,10]
# l = []
# for i in a:
#     if i%2 ==0:
#         l.append(i)
# print(l)        




# a = [1,2,3,4,5,6,8,9,10]
# l = []
# for i in a:
#     if i%2 != 0:
#         l.append(i)
# print(l)        




a = [1,2,3,4,5,6,8,9,10]
l = filter(lambda x : x%2 == 0,a)
print(list(l))