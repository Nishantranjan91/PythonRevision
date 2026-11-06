# a = [12,14,16,23,25,34,37,45,48,59,68,70]
# search = 48
# start = 0
# last = len(a)-1
# mid = (start+last)//2
# while start <= last:
#     if [mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1 
#         mid = (start+last)//2
#     elif    a[mid] > search:
#         last = mid - 1
# else:
#     print("sorry no such elements are exist")    
# 
# 
# 
# 
# a = [12, 14, 16, 23, 25, 34, 37, 45, 48, 59, 68, 70]




# a = [12, 14, 16, 23, 25, 34, 37, 45, 48, 59, 68, 70]

# search = 50

# start = 0
# last = len(a) - 1

# while start <= last:

#     mid = (start + last) // 2

#     if a[mid] == search:
#         print(f"Element found at index {mid}")
#         break

#     elif a[mid] < search:
#         start = mid + 1

#     else:
#         last = mid - 1

# else:
#     print("Sorry, no such element exists.")




# # Binary Search using Iterative Method
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid

#         elif arr[mid] < target:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1


# # Example
# arr = [10, 20, 30, 40, 50, 60, 70]
# target = 40

# result = binary_search(arr, target)

# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")
  




# Binary Search using Recursive Method
def binary_search(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    else:
        return binary_search(arr, low, mid - 1, target)


# Example
arr = [5, 10, 15, 20, 25, 30, 35]
target = 25

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")