# Pair with target sum
'''
Given an array of sorted numbers and a target sum, find a pair in the array
whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such
that they add up to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
'''
def pair_with_targetsum(arr, target_sum):
    pointerEnd = len(arr) - 1
    pointerStart = 0
    runningSum = arr[pointerStart] + arr[pointerEnd]

    while (runningSum != target_sum):
        if (runningSum > target_sum):
            pointerEnd -= 1
        elif (runningSum < target_sum):
            pointerStart += 1
        runningSum = arr[pointerStart] + arr[pointerEnd]

    return pointerStart,pointerEnd

print("pair_with_targetsum (easy)")
print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))

# Remove Duplicates
'''
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates in-place return 
the length of the subarray that has no duplicate in it.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates
will be [2, 3, 6, 9].
'''
def remove_duplicates(arr):
    # one pointer will iterate through the array while another keeps track of where you can place the next non duplicate
    # we return the next non-duplicate var which will equate the count of unique elements
    
    next_non_duplicate = 1
    i = 0

    while (i < len(arr)):
        if arr[i] != arr[next_non_duplicate - 1]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    
    return next_non_duplicate

print("remove_duplicates (easy)")
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))

# Squaring a sorted array
'''
Given a sorted array, create a new array containing squares of all the
numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
'''
def make_squares(arr):
    squares = []
    pointerSmall = 0
    pointerLarge = 1
    # loop through the input
    # pointer will be for the new array - tracking the smallest and largest index - increment or decrement based on the next number
    for i in range(len(arr)):
        temp = arr[i] * arr[i]
        squares[i] = temp
    
    return squares

print(make_squares([-2, -1, 0, 2, 3]))