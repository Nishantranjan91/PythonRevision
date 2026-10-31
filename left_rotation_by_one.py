# a = [10,20,30,40,50,]

# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1], a[i]
# print(a)    


# left rotation by 2
arr = [1, 2, 3, 4, 5]

n = 2

result = arr[n:] + arr[:n]

print(result)