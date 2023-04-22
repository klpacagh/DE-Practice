def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        
        mid = (high + low) // 2
        if arr[mid] < x: # ignore left half
            low = mid + 1
        elif arr[mid] > x: #ignore right half
            high = mid - 1
        else:
            return mid

    return -1

print(binary_search([3,4,1,2,5,6,8,9], 5))