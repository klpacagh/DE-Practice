# start with pivot point (first item), compared to each item after
# swap less than with the first item that was greater than 
# at end of first iteration last point swap the pivot with the last less than item
# so all items less than pivot on left and all greater than pivot on right
# then we do the same operation up to the new pivot index and same operation to the right

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# sets it up so all items less than pivot on left and all greater than pivot on right
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index) # switch final pivot and swap index
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)  # returns index of 3
        # list is now --> small < pivot_index < larger
        quick_sort_helper(my_list, left, pivot_index - 1) 
        quick_sort_helper(my_list, pivot_index + 1, right )
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0 ,len(my_list) - 1)

my_list = [4,6,1,7,3,2,5]
print(quick_sort(my_list))

# process of running pivot is O(n)
# recursive part is O(logn)
# bestcase quicksort is O(nlogn)
# worstcase or Big O is O(n^2) if the data is already sorted - wow!
# -- this is because pivot will need to be run on every item, so the O(n) becomes O(n^2)



