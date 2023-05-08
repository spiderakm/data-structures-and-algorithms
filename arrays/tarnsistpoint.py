"""
Given a sorted array containing only 0s and 1s, find the transition point. 


Example 1:

Input:
N = 5
arr[] = {0,0,0,1,1}
Output: 3
Explanation: index 3 is the transition 
point where 1 begins.
"""

def transitionPoint(arr, n):

    for i in range(n):
        if arr[i] == 1:
            return i
    return -1
#return next((i for i in range(n) if arr[i] == 1), -1)

# optimal solution
def transitionPoint(arr, n):
    res = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == 1:
            res = mid
            end = mid - 1
        elif arr[mid] == 0:
            start = mid + 1
    return res