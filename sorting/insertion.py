#select element and swap untill element got the right position

arr = [5,2,7,1,3,6]
n = len(arr)

for i in range(1,n):
    j = i
    while j > 0 and arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

print(arr)