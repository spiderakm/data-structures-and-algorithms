"""
Given an unsorted array A of size N that contains only positive integers,
 find a continuous sub-array that adds to a given number S 
 and return the left and right index(1-based indexing) of that subarray.
Link -> https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
"""

def subarr(arr,s):
    n = len(arr)
    start = 0
    end = 0
    summ = 0
    while end < n:
        summ += arr[end]
        while summ > s and start <= end:
            summ -= arr[start]
            start += 1
        if summ == s:
            return [start + 1,end + 1]
        end += 1
    return [-1]

arr = [1,2,3,7,5]
s = 12
print(subarr(arr,s))