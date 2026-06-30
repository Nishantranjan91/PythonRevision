# a = [1,1,1,2,2,2,2,3,3,3,3,3,4,4,5,6,6]
# j = set(a)
# print(j)



# a = [1,1,1,2,2,2,2,3,3,3,3,3,4,4,5,6,6]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)            





a = [1,1,1,2,2,2,2,3,3,3,3,3,4,4,5,6,6]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d.keys())  