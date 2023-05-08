"""
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Note: Retun the index of Equilibrium point. (1-based index)

Example 1:

Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 3 
Explanation:  
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2). 
"""

def equilibriumPoint(self,A, N):
        if N == 1:
            return 1
        for i in range(1,N-1):
            if sum(A[:i]) == sum(A[i+1:]):
                return i+1
        return -1


def find_equilibrium_point(n, A):
    total_sum = sum(A)
    left_sum = 0
    for i in range(n):
        temp_sum = total_sum - A[i]
        if left_sum == temp_sum:
            return i+1
        left_sum += A[i]
    return -1

