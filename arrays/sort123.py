"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
"""

# def sort(arr):
#     zero, one, two = [], [], []
#     for i in arr:
#         if i == 0:
#             zero.append(i)
#         elif i == 1:
#             one.append(i)
#         else:
#             two.append(i)
#     arr[:] = zero + one + two
                
def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
 
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
 
    return arr
