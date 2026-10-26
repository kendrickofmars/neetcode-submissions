from typing import List, Deque
from collections import deque
'''
initialization: "queue = deque([1,2,3,4])" - takes a list as an argument
all queue operations except for getting a random element from the queue are O(n)
operations are:
append() - add all the way to the right
popleft() - remove and return leftmost element
peek right queue[-1], peek left queue[0]
len(queue) - check if empty

'''

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    # wrap our list arr as a deque
    queue = deque(arr)
# for every value from 0 to k, we will append and pop, which is equivalent to shifting k units to the left
    for i in range(k):
        queue.append(queue.popleft())

    return queue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
