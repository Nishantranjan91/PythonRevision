# without map function:
a = [2,4,5,8,9]
m = []
for i in a:
    m.append(i**2)
print(m)



# using map function:
def square(x):
    return x**2
a = [1,2,3,4]
l = map(square,a)
print(list(l))