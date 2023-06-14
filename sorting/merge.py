# def m(arr,low,high):
#     if low == high:
#         return
#     mid = (low + high) // 2
#     m(arr,low,mid)
#     m(arr,mid+1,high)
#     return merge(arr,low,mid,high)
    
# def merge(arr,low,mid,high):
#     left = low
#     right = mid + 1
#     res = []
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             res.append(arr[left])
#             low += 1
#         else:
#             res.append(arr[right])
#             right += 1
#     while left <= mid:
#         res.append(arr[left])
#         low += 1
#     while right <= high:
#         res.append(arr[right])
#         right += 1
        
        
#     return arr
    
    
    
    

# arr = [2,8,5,7,3,9,1]
# low = 0
# high = len(arr)-1
# m(arr,low,high)
# # print(res)


def merge_sort(arr):
    # Base case: if the list has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint of the list
    mid = len(arr) // 2

    # Split the list into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    merge_sort(left)
    merge_sort(right)

    # Merge the sorted halves
    merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0

    # Compare elements from the left and right lists and place them in the original list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Add any remaining elements from the left or right list
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


my_list = [5, 3, 8, 2, 1, 7, 6, 4]
merge_sort(my_list)
print(my_list)
