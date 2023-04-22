from random import randrange

def quick_sort_v2(numbers):
    if len(numbers) <= 1:
        return numbers

    left_pivot = []
    right_pivot = []
    pivot = numbers[randrange(len(numbers))] # better to choose a random instead of choosing first number in list
    # pivot = numbers[0]
    numbers.remove(pivot) # to not include in loop
    
    # for num in numbers[1:]:
    for num in numbers:
        if num <= pivot:
            left_pivot.append(num)
        else:
            right_pivot.append(num)

    return quick_sort_v2(left_pivot) + [pivot] + quick_sort_v2(right_pivot)

nums = [4,10,3,6,9,5,25]
print(quick_sort_v2(nums))
