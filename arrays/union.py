"""
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.

Link -> https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?page=2&difficulty[]=0&category[]=Arrays&sortBy=submissions

Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
"""
# bruteforce 
#return sorted(set(a+b))

def findUnion(arr1, n, arr2, m):
    i = j = 0
    union = []
    
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            union.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        else:
            union.append(arr2[j])
            j += 1
    
    while i < n:
        union.append(arr1[i])
        i += 1
    
    while j < m:
        union.append(arr2[j])
        j += 1
    
    return union
