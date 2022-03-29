# bubbling up the largest/smallest items till everything is sorted
# time complexity --> O(n^2)
# space complexity --> O(1) in place

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1): # length of list - 1, get to 0, decrement by 1
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


some_list =[4,2,6,5,1,3]
print(bubble_sort(some_list))