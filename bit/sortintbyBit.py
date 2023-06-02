# sort array using bit
"""
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
"""



arr = [0,1,2,3,4,5,6,7,8]
a = [sum([int(i) for i in bin(j)[2:]]) for j in arr] # count the bit of every element
sort = sorted(zip(a, arr))# adding and sorting the array with amount of bits
print([i[1] for i in sort])
#return the array