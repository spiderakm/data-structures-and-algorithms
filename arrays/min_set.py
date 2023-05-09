"""
Given an array of distinct positive numbers, the task is to calculate the minimum number of subsets (or subsequences) from the array such that each subset contains consecutive numbers.
 

Example 1:

Input:
N = 10
Arr[] = {100, 56, 5, 6, 102, 58, 101, 57, 7, 103} 
Output:
3
Explanation:
{5, 6, 7}, { 56, 57, 58}, {100, 101, 102, 103} are
3 subset in which numbers are consecutive.
"""

#User function Template for python3

class Solution:
    def numofsubset(self, arr, n):
        # Your code goes here
        arr.sort()
        c = 1
        for i in range(len(arr)-1):
            if arr[i] + 1 == arr[i+1]:
                continue
            else:
                c += 1
        return c





    
# } Driver Code Ends