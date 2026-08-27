# a = [1,2,3,4,5]
# l = []
# for i in a:
#     l.append(i**2)
# print(l)    




a = [1,2,3,4,5]
l = map(lambda x :x**2,a)
print(list(l))