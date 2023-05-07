"""
Given a sorted array A[] of size N, delete all the duplicated elements from A[]. Modify the array such that if there are X distinct elements in it then the first X positions of the array should be filled with them in increasing order and return the number of distinct elements in the array.

Link -> https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: {2}
Explanation: After removing all the duplicates 
only one instance of 2 will remain.
"""

def remove_element(arr):
    # return list(set(arr))
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[j] = arr[i]
            j += 1
    return j,arr

arr = [1,2,2,3,3,3]
print(remove_element(arr))