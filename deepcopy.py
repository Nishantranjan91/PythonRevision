import copy
a = [10,20,30,40]

b = copy.deepcopy(a)

b[0]=100

print(a)
print(b)