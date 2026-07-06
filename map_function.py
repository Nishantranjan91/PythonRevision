a = [1,2,3,4]
l = []
for i in a :
    l.append(i**2)
print(l)    



def square(x):
    return  x**2
a = [1,2,3,4]
l = map(square,a)
print(list(l))