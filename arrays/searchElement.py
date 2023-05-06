#Given an integer array and another integer element. The task is to find if the given element is present in array or not.


# bruteforce solution Time Complexty --- O(n)
def search(self,arr, N, X):
    #Your code here
    for i in range(len(arr)):
        if arr[i] == X:
            return i
    return -1