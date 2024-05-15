def binary(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) 
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary(arr, target, low, mid - 1)
    else:
        return binary(arr, target, mid + 1, high)


arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = binary(arr, target, 0, len(arr)-1)
print("Index of", target, "in array:", result)