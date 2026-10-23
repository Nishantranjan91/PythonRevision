# a = [12,34,98,76,49,30,490,23,21,99]
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)            





# a = [12,34,98,76,49,30,490,23,21,99]
# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)   




# Deep copy of a nested list
import copy

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

original[0][0] = 100

print("Original list:", original)
print("Copied list:", copied)