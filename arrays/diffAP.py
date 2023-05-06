#Find the missing element from an ordered array arr[], consisting of N elements representing an Arithmetic Progression(AP).
# proble link - https://practice.geeksforgeeks.org/problems/missing-element-of-ap2228/1?page=2&difficulty[]=0&status[]=solved&category[]=Arrays&sortBy=submissions
# Input:
# N = 6
# Arr[] = {2, 4, 8, 10, 12, 14}
# Output: 6
# Explanation: Actual AP should be 
# 2, 4, 6, 8, 10, 12, 14.


# bruteforce with linear search TL - O(N)
def findMissing(arr):
    # we have to find difference b/w the AP
    n = len(arr)
    diff = (arr[0] + arr[n-1]) // n
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != diff:
            return arr[i] + diff

print(findMissing([2,4,8,10,12,14]))


# optimize with binary search TL - logn
def findMissing(arr):
    n = len(arr)
    diff = (arr[0] + arr[n-1]) // n
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[0] + diff*mid:
            left = mid + 1
        else:
            right = mid

# tricky 1
        # TOTAL = (N+1)/2 * (ARR[0]+ARR[N-1])
        # PRINT(TOTAL)
        # FOR  I IN ARR:
        #     TOTAL -= I
        # RETURN INT(TOTAL)
# tricky 2
def findMissing(arr):
    n = len(arr)
    expected_sum = (n+1)*(arr[0]+arr[n-1])//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum