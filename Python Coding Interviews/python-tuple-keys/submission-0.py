from typing import List, Set, Tuple

'''
we can store a tuple as a key in a dictionary because they are immutable. Example:

dict_of_pairs = {}

dict_of_pairs[(0,0)] = 1
dict_of_pairs[(0,1)] = 2

print(dict_of_pairs) # {(0, 0): 1, (0, 1): 2}

# just the tuple key, no values can be associated with it
set_of_pairs = set()
set_of_pairs.add((0, 0))
set_of_pairs.add((0, 1))

print(set_of_pairs) # {(0, 0), (0, 1)}
'''



def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    # initializing and empty set of int tuples
    set_of_tuples = set(())
    # nested for loop to go through list of sublists
    # from 0 to length of list of lists
    for row in range(len(grid)):
        # from 0 to length of sublist
        for column in range(len(grid[0])):
            # use set lookup for O(1) operation to check if 1 is in sublist
            # check if each element is 1
            if grid[row][column] == 1:
                set_of_tuples.add((row, column))


    



    return set_of_tuples


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
