from typing import List, Deque
from collections import deque

'''
deques have all the operations that queues have but they can also append to the left side of the queue,
and they can pop from the right, not just the left. 
appendleft and pop are constant time operations O(1)
'''

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)

    # for i from 0 to k
    for i in range(k):
        queue.appendleft(queue.pop())
    
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
