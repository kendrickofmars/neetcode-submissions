from typing import List, Set

'''
set comprehension is identical to dictionary comprehension syntactically, just no value to associate with the key
nums = [1,3,5]
squared = {num * num for num in nums}
'''


def double_nums(nums: List[int]) -> Set[int]:
    # initializing an empty set to hold doubled values from set comprehension
    doubled_nums_set = set()

    doubled_nums_set = {num * 2 for num in nums}

    return doubled_nums_set


# do not modify below this line

output1 = double_nums([1, 2, 3])
print(type(output1)) 
print(sorted(list(output1)))

output2 = double_nums([4, -2, 0, 7])
print(type(output2)) 
print(sorted(list(output2)))

output3 = double_nums([10, 20, 30, 40, 50])
print(type(output3)) 
print(sorted(list(output3)))
