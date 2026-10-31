arr = [10, 20, 30, 40, 50, 60]

n = 2

for i in range(n):
    first = arr.pop(0)
    arr.append(first)

print(arr)