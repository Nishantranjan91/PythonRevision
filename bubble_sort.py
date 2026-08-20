# a = [12,34,98,76,49,30,490,23,21,99]
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)            





a = [12,34,98,76,49,30,490,23,21,99]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)   