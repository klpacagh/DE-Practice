# maxSumSubArray of size N
def maxSumSubArray(the_array, subarray_size):
    max_value = 0
    current_running_sum = 0
    k = subarray_size

    for i in range(len(the_array)):
        current_running_sum += the_array[i]

        if (i >= k - 1):
            max_value = max(max_value, current_running_sum)
            current_running_sum -= the_array[i - (k - 1)] # subtracts leftmost value from subarray 3

    # print(current_running_sum)
    print("MaxSum Subarry of size: ", subarray_size, " is ", max_value)

my_array = [4,2,1,7,8,1,2,8,1,0]

maxSumSubArray(my_array, 3) # returns 16

#--------------------------------------------------------

#smallestSubarrayGivenSum (smallest subarray where the target sum is N) 
# --> dynamic window where the window shrinks and expands while keeping to the target sum
# shrink when current is > target, expand when current is < target

def smallestSubArrayGivenSum(the_array, targetSum):
    window_start = 0
    current_window_sum = 0
    min_size_of_window = 100

    for i in range(len(the_array)):
        current_window_sum += the_array[i] # add to running sum as we iterate
        
        window_end = i
        
        while (current_window_sum >= targetSum): # if running sum is >= target sum, we begin to shrink
            min_size_of_window = min(min_size_of_window, window_end - window_start + 1) # (window_end - window_start + 1) gives delta of how large the window is
            current_window_sum -= the_array[window_start] # shrinking window size
            window_start += 1 # move the starting window pointer forward everytime we shrink the window
        
    print("Smallest window size with target of 8 is: ", min_size_of_window)

smallestSubArrayGivenSum([4,2,1,7,8,1,2,8,1,0], 8)

#--------------------------------------------------------

#longestSubstringLenWithKDistinctChars

def maxSubstringLenWithKDistinctChars(the_array, n_distinct_chars):
    my_dict = {}
    K = n_distinct_chars
    window_start = 0
    maxLengthOfWindow = 0

    for i in range(len(the_array)):
        key = the_array[i]
        window_end = i

        if key in my_dict:
            my_dict[key] = my_dict.get(key) + 1
        else:
            my_dict[key] = 1

        while (len(my_dict.keys()) > K):
            # print("window start: ", window_start, " window end: ", window_end)
            maxLengthOfWindow = max(maxLengthOfWindow, window_end - window_start)
            # print(maxLengthOfWindow, ( window_end - window_start))
            my_dict[the_array[window_start]] = my_dict.get(the_array[window_start]) - 1
            if (my_dict.get(the_array[window_start]) == 0):
                del my_dict[the_array[window_start]]
            window_start += 1
            # print(my_dict)
            # print("----")
            
    print('Max Length of Substring with', n_distinct_chars, ' distinct chars: ', maxLengthOfWindow)

maxSubstringLenWithKDistinctChars(['A','A','A','H','H','I','B','C'], 2)




#----------------- Grokking

print("\nGROKKING!!! BELOW")
# Maximum Sum of Subarray of Size K
'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''

def max_sub_array_of_size_k(k, arr):
    largest = 0
    windowStart = 0
    runningSum = 0
    windowCurrSize = 0

    for windowEnd in range(len(arr)):
        windowCurrSize += 1
        runningSum += arr[windowEnd]
        
        if runningSum > largest:
            largest = runningSum 

        if (windowCurrSize > k - 1):

            # subtract start
            runningSum -= arr[windowStart]
            windowStart += 1
            windowCurrSize -= 1

    return largest

max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])

# Smallest Subarray With a Greater Sum
'''
Given an array of positive numbers and a positive number ‘S,’ find
the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
'''

def smallest_subarray_with_given_sum(s, arr):
    smallest_subarray_len = 999
    windowStart = 0
    rollingSum = 0

    for windowEnd in range(len(arr)):
        rollingSum += arr[windowEnd]

        while (rollingSum > s):
            # print("we - ws = ", windowEnd - windowStart)
            if (windowEnd - windowStart) < smallest_subarray_len and (windowEnd - windowStart > 0):
                smallest_subarray_len = windowEnd - windowStart 
            rollingSum -= arr[windowStart]
            # print("shrink sum: ", rollingSum)
            windowStart += 1

    return smallest_subarray_len

smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])

# Fruits into Baskets
'''
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. 
You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
'''

def fruits_into_baskets(fruits):
    limit = 2
    my_dict = {}
    window_start = 0
    longest = 0

    for window_end in range(len(fruits)):
        key = fruits[window_end]
        
        if key in my_dict:
            my_dict[key] = my_dict.get(key) + 1
        else:
            my_dict[key] = 1

        while(len(my_dict) > 2):
            my_dict[fruits[window_start]] = my_dict.get(fruits[window_start]) - 1
            if (my_dict.get(fruits[window_start]) == 0):
                del my_dict[fruits[window_start]]
            window_start += 1
        if (window_end - window_start) + 1 > longest:
            longest = (window_end - window_start) + 1

    # print(my_dict)
    return longest
    


print("fruits into a basket problem: ", fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))


# Longest Substring with Only Distinct Characters
'''
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

'''
def non_repeat_substring(str):
    temp = str
    my_dict = {}
    window_start = 0
    maxLengthOfWindow = 0

    for i in range(len(temp)):
        key = temp[i]
        window_end = i

        if key in my_dict:
            my_dict[key] = my_dict.get(key) + 1
        else:
            my_dict[key] = 1
    
   
        while (my_dict[key] > 1):
            maxLengthOfWindow = max(maxLengthOfWindow, window_end - window_start)
            # print(my_dict.get(temp[window_start]) - 1)
            my_dict[temp[window_start]] = my_dict.get(temp[window_start]) - 1
            if (my_dict.get(temp[window_start]) == 0):
                del my_dict[temp[window_start]]
            window_start += 1

    # print(maxLengthOfWindow)
    return maxLengthOfWindow
print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abccde")))