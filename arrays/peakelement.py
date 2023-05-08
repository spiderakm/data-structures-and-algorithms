"""
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 
problem link -> https://practice.geeksforgeeks.org/problems/peak-element/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions
Input: 
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Generated Output: 1
"""

def peak_element(arr):
    # return arr.index(max(arr))
    maxx = 0
    for i in arr:
        if i > maxx:
            maxx = i
    return 

arr = [1,2,3]
print(peak_element(arr))