a = [10,15,20,25,30,35,40,45,50]
search = 30
for i in range(len(a)):
    if a[i] == search:
        print(f"element fount at index {i}")
        break
else:
    print("sorry no search element is exist.")    