"""
Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

 

Example 1:

Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5
"""

class Solution:
    def segregateElements(self, arr, n):
        pos = []
        neg = []
        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        arr[:] = pos[:] + neg[:]
        