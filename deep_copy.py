# import copy
# a = [10,20,30,40,50]
# b = copy.deepcopy(a)
# b[2] = 1000
# print(a)
# print(b)





import copy
a = [[10,20],[30,40]]
b1 = a.copy()
b2 = copy.deepcopy(a)
b1 = [0][0] = 999
b2 = [1][0] = 888
print(a)
print(b1)
print(b2)