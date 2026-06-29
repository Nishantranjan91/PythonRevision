a = [12,14,16,23,25,34,37,45,48,59,68,70]
search = 48
start = 0
last = len(a)-1
mid = (start+last)//2
while start <= last:
    if [mid] == search:
        print(f"element found at index {mid}")
        break
    elif a[mid] < search:
        start = mid + 1 
        mid = (start+last)//2
    elif    a[mid] > search:
        last = mid - 1
else:
    print("sorry no such elements are exist")            