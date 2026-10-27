import heapq
from typing import List

'''
heaps/priority queues allow us to push/pop (aka insert/remove) elements based on priority given to each element.
In python a heap is a min heap by default, so element w/ smallest priority is at the top of the heap. 
Example:

import heapq
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
print(heap[0]) # 1

# time complexity of a heappush is O(log(n))
heapq.heappush(heap, 0)
# accessing smallest priority element is O(1)
print(heap[0]) # 0

#space complexity is O(n), scales with heap size

'''


def heap_push(heap: List[int], value: int) -> int:
    # heappush takes in the heap we want to push to (as a list), and the element to push
    heapq.heappush(heap, value)

    # heap stores lowest priority element on the top, so return element at index 0
    return heap[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
