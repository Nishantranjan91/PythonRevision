# a = [21,34,45,56,67,78,39,22,44,98,101,234]
# for i in range(len(a)-1):
#     j = i+1
#     min = i
#     for k in range(j,len(a)):
#         if a[k] < a[min]:
#             min = k
#     a[i],a[min] = a[min],a[i]
# print(a)            




#Sort numbers in ascending orde

# numbers = [64, 25, 12, 22, 11]

# n = len(numbers)

# for i in range(n):
#     min_index = i

#     for j in range(i + 1, n):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# print("Sorted list:", numbers)





# Sort numbers in descending order

numbers = [5, 2, 9, 1, 7]

n = len(numbers)

for i in range(n):
    max_index = i

    for j in range(i + 1, n):
        if numbers[j] > numbers[max_index]:
            max_index = j

    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print("Sorted list:", numbers)
