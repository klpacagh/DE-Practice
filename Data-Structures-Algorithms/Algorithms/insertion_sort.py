# compare item with the item's before it
# time complexity --> O(n^2), best case is O(n) if almost sorted already
# space complexity --> O(1) in place
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

some_list =[4,2,6,5,1,3]
print(insertion_sort(some_list))