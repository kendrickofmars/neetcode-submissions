import heapq
from typing import List

'''

a heappop is a big O(log(n)) operation, where n is elements in the heap

import heapq

heap = []

heapq.heappush(heap, "banana")
heapq.heappush(heap, "apple")
heapq.heappush(heap, "kiwi")

print(heapq.heappop(heap))  # apple
print(heapq.heappop(heap))  # banana
print(heapq.heappop(heap))  # kiwi

The reason we pop apple first, is because by default string priority is lexicographical, so apple < banana < kiwi 

If we try to pop from empty heap we get an IndexError

'''



def heap_pop(heap: List[int]) -> List[int]:
    # declare new heap to hold popped elements
    popped_heap_elements = []
    # loop through and pop every element in the old heap
    for i in range(len(heap)):
        # heapify, and then whatever value we popped from heap, we push it to popped_heap_elements
        heapq.heappush(popped_heap_elements, heapq.heappop(heap))



    return popped_heap_elements


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
