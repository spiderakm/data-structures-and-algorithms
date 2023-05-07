"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row."""

"""
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""
# bruteforce O(n2)
# def search(matrix,target):
#     for i in matrix:
#         if target in i:
#             return True
#     return False

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# print(search(matrix,target))



#binary search
def search(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n -1
    print(right)
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False





matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search(matrix,target))