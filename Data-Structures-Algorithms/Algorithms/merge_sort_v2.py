def merge_sort_v2(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers)//2
    left_pointer, right_pointer = 0,0
    left_list = merge_sort_v2(numbers[:mid]) # recursively build left list in sorted order
    right_list = merge_sort_v2(numbers[mid:]) # recursively build right list in sorted order
    sorted_list = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            sorted_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right_list[right_pointer])
            right_pointer += 1
    
    # handle if one list becomes empty
    sorted_list += left_list[left_pointer:] # when pointer equal to length of list then appends empty list
    sorted_list += right_list[right_pointer:]

    return sorted_list



nums = [4,10,3,6,9,5,25,104,1,55,81]
print(merge_sort_v2(nums))