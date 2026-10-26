from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    # list to hold largest element in each sublist
    max_values_list = []

    # iterate over each list in the list using index value
    for sublist in nested_arr:
        # initialize a default comparison value using first element in each sublist
        maximum_in_arr = sublist[0]
        # inner loop through each element in the sublist
        for element in sublist:
            # make comparison using max, assign that value to maximum_in_arr
            maximum_in_arr = max(maximum_in_arr, element)    
        # append value to max_values_list after each run
        max_values_list.append(maximum_in_arr)
    return max_values_list



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
