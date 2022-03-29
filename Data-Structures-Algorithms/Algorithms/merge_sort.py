# break list in half again and again until there are lists with 1 item in them
# then merge pairs into a sorted lists, then merge those sorted lists, etc. until you get one sorted list
# at final part where its last 2 lists, keep going until one of the list is empty to where you can just append the remaining list

# space complexity --> O(n), out of place sorting, creates new lists
# time complexity --> breaking apart is O(logn) and putting togther is O(n) --> O(nlogn)

def merge(list1, list2): # helper function
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2): # as long as lists both have items in them
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else: # if j is less
            combined.append(list2[j])
            j += 1

    while i < len(list1): # if any remaining in list i
        combined.append(list1[i])
        i += 1

    while j < len(list1):
        combined.append(list2[j]) # if any remaining in list j
        j += 1

    
    return combined


# break lists in half, base case:L when len(list) is 1, then use merge to put lists together

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = int(len(my_list) / 2)
    left = my_list[:mid] # index from 0 up to not including mid
    right = my_list[mid:] # index from mid to end of list
    
    # remember, merge only takes sorted lists
    return merge(merge_sort(left),merge_sort(right))



print(merge_sort([3,1,4,2]))