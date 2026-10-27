import heapq
from typing import List

'''
we can heapify a list using heapq.heapify(list_name). Elements in the list get rearranged to form a valid heap.
By default this is a min heap.

e.g. 
list = [4,3,2,1]
# this operation is O(n). It's faster than pushing elements 1 by 1 onto heap, which is O(nlogn)
heapq.heapify(list)

while list:
    print(...) # 1\n 2\n 3\n 4

'''

def heapify_strings(strings: List[str]) -> List[str]:
    # heapify the strings list into a default min heap
    heapq.heapify(strings)
    return strings


def heapify_integers(integers: List[int]) -> List[int]:
    # heapify integers to default min heap
    heapq.heapify(integers)
    return integers


def heap_sort(nums: List[int]) -> List[int]:
    # min heap, but reverse the output so high pri first shown
    heapq.heapify(nums)
    nums = sorted(nums)
    return nums

    


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
