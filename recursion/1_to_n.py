"""
Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10
"""

def printNos(self,N,i=0):
        #Your code here
    if N == 0:
        return
    self.printNos(N-1)
    print(N,end=" ")

def a(n,i=0):
    if i > n:
        return
    print(i)
    i+=1
    a(n,i)
        