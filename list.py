# reference copy:
# a = [11,12,13,14,15]
# b = a
# b[0] = 111
# print(a)
# print(b)




# shallow copy:
# a = [11,12,13,14,15]
# b = a.copy()
# b[0] = 111
# print(a)
# print(b)


# deep copy:
import copy
a = [10,20,30,40]
b = copy.deepcopy(a)
b[0] = 100
print(a)
print(b)

