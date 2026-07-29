# a = [12,13,14,15,16,17,14,23,24,25,36,78,90]

# for i in range(len(a)):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted.")
#         break
# else:
#     print("your list is sorted")     





b = [12,13,14,15,16,17,14,23,24,25,36,78,90,100,200]

for i in range(len(b)):
    if b[i] < b[i+1]:
        continue
    else:
        print("your list is not sorted.")
        break
else:
    print("your list is sorted") 