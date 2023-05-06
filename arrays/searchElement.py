#Given an integer array and another integer element. The task is to find if the given element is present in array or not.

# Input:
# n = 4
# arr[] = {1,2,3,4}
# x = 3
# Output: 2


# bruteforce solution Time Complexty --- O(n)
def search(arr, X):
    #Your code here
    for i in range(len(arr)):
        if arr[i] == X:
            return i
    return -1

arr = [1,2,3,4,5,6]
print(search(arr, 5))

    # optimize binary search
def search(arr, X):

    start = 0
    end = len(arr) - 1
    mid = 0
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            start = mid + 1
        else:
            end = mid - 1
    return -1     

arr = [1,2,3,4,5,6]
print(search(arr, 5))