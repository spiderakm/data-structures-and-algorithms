"""Given a binary array A[] of size N. The task is to arrange the array in increasing order.
Note: The binary array contains only 0  and 1.
 

Example 1:

Input: 
5
1 0 1 1 0

Output: 
0 0 1 1 1

Explanation: 
After arranging the elements in 
increasing order, elements will be as 
0 0 1 1 1."""

# first bruteforce nlogn
# arr.sort()

def binsort(arr):
    coutn_one = 0
    count_zero = 0
    for i in arr:
        if i == 0:
            count_zero += 1
        else:
            coutn_one += 1
    for i in range(count_zero):
        arr[i] = 0
    for i in range(coutn_one,len(arr)):
        arr[i] = 1
    return arr



b = [1,0,1,1,0]
print(binsort(b))