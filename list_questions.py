# sum and average of a list:
# a = [10,20,30,40,50]
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)    
# print((sum)/len(a))




# maximum element with index:
# a = [10,12,23,45,42,11,38,55,99,68,81]
# max = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"maximum element is {max} and at index {index}")        





# a given list is sorted or not:
# a = [10,12,23,45,42,11,38,55,99,68,81]
# for i in range(len(a)):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("your list is not sorted.")
#         break
# else:
#     print("your list is sorted.")    



# Left rotation by one:
# a = [10,12,23,45,42,11,38,55,99,68,81] 
# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1],a[i]
# print(a)    





# # right rotation:
# a = [10,12,23,45,42,11,38,55,99,68,81]
# for i in range(len(a)-1,0,-1):
#     a[i],a[i-1] = a[i-1],a[i]
# print(a)    




# k times rotation:
# k = int(input("how many times you want to rotate ? :-"))
# a = [10,12,23,45,42,11,38,55,99,68,81]
# for i in range(k):
#     for i in range(len(a)-1):
#         a[i],a[i+1] = a[i+1],a[i]
# print(a)        




# reverse the list:
# a = [10,12,23,45,42,11,38,55,99,68,81]
# b = []
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)    





# linear search:
a = [10,12,23,45,42,11,38,55,99,68,81]
search =99
for i in range(len(a)):
    if a[i] == search:
        print(f"the element is at index {i}")
        break
else:
    print("sorry no such element is exist")




# Binary search:
a = [12,14,16,23,25,34,37,45,48,59,68,70]
search = 48
start = 0
last = len(a)-1
mid = (start+last)//2
while start <= last:
    if a[mid] == search:
        print(f"element found at index {mid}")
        break
    elif a[mid]<search:
        start = mid+1
        mid = (start+last)//2
    elif a[mid]>search:
        last = mid - 1
        mid = (start+last)//2
else:
    print("Sorry no such element is exist")          