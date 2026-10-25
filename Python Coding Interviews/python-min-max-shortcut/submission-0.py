from typing import List


def disallow_negatives(num: int) -> int:
    # if num is greater than or equal to 0 just return the number
    return max(0, num)


def max_difference(nums: List[int]) -> int:
    # will contain the difference and update once greater value is found
    greatest_diff = 0
    for i in range(len(nums) - 1):
        # subtract left from right for every item in nums and store that in sub_default
        greatest_diff = max(greatest_diff, nums[i+1] - nums[i])

    # return value will always be positive, no need to worry about returning negative values
    return greatest_diff



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
