# arr = [10, 20, 30, 40, 50, 60]

# n = 2

# for i in range(n):
#     last = arr.pop()
#     arr.insert(0, last)

# print(arr)




arr = [1, 2, 3, 4, 5]

n = 2

result = arr[-n:] + arr[:-n]

print(result)