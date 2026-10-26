from typing import List

'''
if we want row and column width in a 2D list, we can use len like so:
    rows = len(grid)
    cols = len(grid[index of sublist])

'''

def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    # holds bool value for whether we're inbounds or not
    inbounds = None

    # since number of columns will be the same for each row, we only need the first column-length for the first row
    rows, cols = len(grid), len(grid[0])

    # check if r and c are in bounds
    if 0 <= r < rows and 0 <= c < cols:
        inbounds = True
    else:
        inbounds = False

    return inbounds


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
