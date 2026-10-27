class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # declare a hashset to hold all unique values
        hash_set = set()
        # loop through and add every value in nums to hash_set
        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set.add(num)
        return False
        
        