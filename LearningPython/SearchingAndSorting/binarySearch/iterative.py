def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = int((high + low)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid
    return -1
arr = [1,2,3,12,34,33]
x = 12
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index ", str(result))
else:
    print("Element is not present")

# Iterative way for the binary search 
# Time Complexity - O(logn)
# Space Complexity - O(1)