import heapq
from typing import List

'''
To simulate max heap, we can negate the values inserted into the heap. The further away from 0, the higher the priority.

e.g: 
nums = [4,2,3,5]
max_heap = []

for num in nums:
    # negating the value before pushing onto our heap
    heapq.heappush(max_heap, -num)
# while there are elements still on the heap
while max_heap:
    top = -heapq.heappop(max_heap)
    print(top) # 5\n 4\n 3\n 2
'''


def get_reverse_sorted(nums: List[int]) -> List[int]:

    # initialize the empty list which will be heapified after pushing to it
    max_heap = [] 
    # declare empty list to add greatest values to 
    new_heap = []
    # looping through list values
    for num in nums:
        heapq.heappush(max_heap, -num)
    
    # while the heap is not empty
    while max_heap:
        # pushing back onto the same heap, the negated values that we popped
        new_heap.append(-heapq.heappop(max_heap))

    return new_heap




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
