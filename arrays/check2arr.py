#Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
#proble link - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be 
# rearranged to {0,1,2,4,5}

# bruteforce solution TC - nlogn

def check(A,B):
    if len(A) == len(B):
        arrA = sorted(A)
        arrB = sorted(B)
        for i in range(len(A)):
            if arrA[i] != arrB[i]:
                return 0
        return 1
    return 0

A = [1,2,5,4,0]
B = [2,4,5,0,1]
print(check(A,B))



def check(A,B):
    if len(A) != len(B):
        return False
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i in B:
        if i not in count or count[i] == 0:
            return False
        else:
            count[i] -= 1
    return True


A = [1,2,5,4,0]
B = [2,4,5,0,1]
print(check(A,B))