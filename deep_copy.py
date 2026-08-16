import copy
a = [10,20,30,40,50]
b = copy.deepcopy(a)
b[2] = 1000
print(a)
print(b)