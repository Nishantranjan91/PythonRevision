a = [19,30,49,40,48]
for i in range(len(a)-1,0,-1):
    a[i], a[i-1] = a[i-1],a[i]
print(a)    