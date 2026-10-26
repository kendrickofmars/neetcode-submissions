from collections import defaultdict
from typing import List, Dict

'''
defaultdict's purpose is to remove the need to check if an element exists in a dictionary, and will assign a defaultvalue dependent on what datatype you feed it, so for freq = defaultdict(int), the default value is 0. 
If it was list, we would do d = defaultdict(list), the default value would be an empty list

example
nums = [1,2,3,4,1]
for num in nums:
    # at index in empty list, append a value of num to that index to create a index-list(value) pair
    d[num].append(num)
print(d) : # {1: [1,1], 2: [2,2], 4: [4], 3:[3]} # adds item to empty list d for as many occurrences as there are in nums
'''


def count_chars(s: str) -> Dict[str, int]:
    # create an empty dictionary to append char : count to. Default value will be an int = 0
    char_count_dict = defaultdict(int)
    # for chars c in string s, add the char: count tuple
    for c in s:
        char_count_dict[c] += 1

    return char_count_dict


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    # declare an empty dictionary with default list value as arg, where the keys will be the 1st element of each list
    # values will be the rest of the elements in the list e.g. [[1,2,3], [4,5,6] , [1,4]] 
    # output would be 1: [2,3,4], 4:[5, 6]
    first_el_to_rest_el = defaultdict(list)
    # looping through list of lists
    for sublist in nums:
        # looping through the 2nd element of the sublist onward
        for i in range(1, len(sublist)): 
            # then append the remaining elements of the list as the values
            first_el_to_rest_el[sublist[0]].append(sublist[i])
    return first_el_to_rest_el
            
# This is a O(n^2) time complexity solution because of the nested for loops

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
