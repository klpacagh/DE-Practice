
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

maxSumSubArray(my_array, 3)