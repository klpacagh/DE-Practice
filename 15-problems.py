#------------ print prime numbers btwn 100 and 200

# for num in range(1,10):
#     if (all(num % i != 0 for i in range(2, num))):
#         print(num)


#------------ sort elements in a list
# my_list = [24,55,76,64,25,12,22,11,1,2,44,3,122,23,24]
# new_list = []
# while my_list:
#     min = my_list[0]
#     for x in my_list:
#         if x < min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)

# print(new_list)


#------------ fibonacci seq
# 0,1,1,2,3,5 ...

# def fibSeq(n):
#     # base case
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     return fibSeq(n-1) + fibSeq(n-2)

# for i in range(0,10):
#     print("fib series of 10: ", fibSeq(i))

#------------ fibonacci seq - dictionary, optimized verion

# fib_dict = {1:0, 2:1, 3:1}

# def fibSeq(n, fib_dict = {1:0, 2:1, 3:1}):
#     # base case
#     if n in fib_dict:
#         return fib_dict[n]
    

#     fib_dict[n] = fibSeq(n-1, fib_dict) + fibSeq(n-2, fib_dict)
#     return fib_dict[n]

# print("fib series of 10: ", fibSeq(10, fib_dict))

#----------- print list in reverse
my_list = [1,2,3,4,5]

# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i])

# print(my_list[::-1])

#----------- palindrome

# def isPalindrome(s):
    # rev = ''.join(reversed(s))
    # rev = s[::-1]
    # str = ""
    # for i in range(len(s) - 1, -1, -1):
    #     str += s[i]
    
    # if (s == rev):
    #     return True
    # else:
    #     return False

# print(isPalindrome("madam"))


#----------- print set of duplicates in list
l = [1,2,2,3,4,4,5,6]
print(set([x for x in l if l.count(x) > 1]))

#----------- print number of words ina  given sentence

# sentence = "sup man"
# print(len(sentence.split(" ")))


#----------- given array of n elements, search a given element x in array

# def search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i

    # return "Not present in array"

# print(search([2,4,5,1], 2))


#----------- implement a binary search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

print(binary_search([3,4,1,2,5,6,8,9], 5))

#----------- python program to extract digits from given string
# test_string = "1w3e4r51efiwne21"
# res = ''.join(filter(lambda i: i.isdigit(), test_string))
# print("the digits of the string are: " + str(res))


#----------- given a string, delete reoccuring chars and return new string

# def deleteReoccurringChars(word):
#     seenChars = set()
#     result = ''
#     for char in word:
#         if char not in seenChars:
#             seenChars.add(char)
#             result += char

#     return result

# print(deleteReoccurringChars("eemotomezzeeeetom"))


'''
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations 
are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.
'''



# def combinationSum(candidates, target):
#     res = []
#     candidates.sort()
#     dfs(candidates, target, 0, [], res)
#     return res
    
# def dfs(nums, target, index, path, res):
#     if target < 0:
#         return  # backtracking
#     if target == 0:
#         res.append(path)
#         return 
#     for i in range(index, len(nums)):
#         dfs(nums, target-nums[i], i, path+[nums[i]], res)


# print(combinationSum([2,3,6,7], 7))


a = {3,4,1,2}
b = {3,1,2,4,5}
print(b.difference(a))
print(b - a)

a = [3,4,1,2]
b = [3,1,2,4,5]
print(set(b) - set(a))
print(sum(b) - sum(a))