from typing import List, Dict

'''
dict comprehension example
nums = [1,2,3,4,5]
to square each element num and assign that to the value, using num as the key in our dictionary 
squared = {num: num * num for num in nums}

'''
def num_to_index(nums: List[int]) -> Dict[int, int]:
    # dict comprehension to set keys as num_to_index elements, and their indices as the values
    nums_dictionary = {num: nums.index(num) for num in nums}

    return nums_dictionary


# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))
