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
a = [10,12,23,45,42,11,38,55,99,68,81] 
for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]
print(a)    
