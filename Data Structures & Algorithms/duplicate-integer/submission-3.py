class Solution:
    # What we want, is a solution that's space and time efficient
    # using what's known as a hashset, we can have a mutable array of only unique strings, numbers,  and tuples, unordered. The values are organized by hash. 
    def hasDuplicate(self, nums: List[int]) -> bool:
        #declaring empty hash set, list within would have '[]' surrounding them -> set([1,2,3,4])
        hash_set = set()
        for i in nums:
            # if the value is unique, return True immediately
            if i in hash_set:
                return True
            # use add to add, remove to delete (raises error if dne), discard to delete (no error if dne),
            # and pop to remove and return a random element
            # add to hash_set if i isn't already present
            hash_set.add(i)
        # if we get through the entire list and there are no duplicates, we return False
        return False

        
        
            
