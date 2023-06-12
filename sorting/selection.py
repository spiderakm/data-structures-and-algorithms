# select the minimum elemnet and swap

arr = [5,1,6,2,3]
n = len(arr)

for i in range(n-2):
    minn = i
    for j in range(i, n):
        if arr[j] < arr[minn]:
            minn = j
    arr[i], arr[minn] = arr[minn], arr[i]


print(arr)