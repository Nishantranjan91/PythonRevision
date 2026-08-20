a = [1,3,23,24,45,46,48,55,59,60,61,62,63,72,74,80]
search = 48
start = 0
last = len(a)-1
mid = (start+last)//2
while start <= last:
    if a[mid] == search:
        print(f"element find at endex {mid}")
        break
    elif a[mid] < search:
        start = mid + 1
        mid = (start + last)//2
    elif a[mid] > search: 
        last = mid - 1
        mid = (start+last)//2
    else:
        print("sorry no such element is exist.")      
