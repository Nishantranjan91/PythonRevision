
k = int(input("how many times you wants to rotate: "))
a = [10,20,30,40,50,60]
for i in range(k):
    for i in range(len(a)-1):
        a[i],a[i+1] = a[i+1],a[i]
print(a)        