from typing import List
'''
using nested list comprehension we can do the following to initialize nested lists with known bounds:
grid = [[0 for i in range(3)] for j in range(2)] - initializing a 2D grid of length 2x3 (rxc)
grid = [[0] * 3 for _ in range(2)] - same as above, but '_' indicates a throwaway variable that won't be used beyond the initialization
initialization of this 2D grid of size n x m with a given value's time complexity is O(n x m)
'''

def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    # given value, c cols long for inner list bounds, r rows long for outer list
    nested_list_given_bounds = [[value] * cols for _ in range(rows)]

    return nested_list_given_bounds


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
