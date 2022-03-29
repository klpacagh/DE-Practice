# keep track of index where minimum value is --> min_index
# when one pass through is done, we swap out the first element with the value of the array using the min_index
# time complexity --> O(n^2)
# space complexity --> O(1) in place

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)): # start, end
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index: # only swap if min value is not already in place
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


some_list =[4,2,6,5,1,3]
print(selection_sort(some_list))
