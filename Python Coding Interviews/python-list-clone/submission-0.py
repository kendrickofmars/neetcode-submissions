from typing import List
"""copying is a O(n) time operation, where n is the size of the list being copied
    operations for regular copy of primitives can be shallow,
    but when copying nested lists, we must use deepcopy()"""

def remove_element(arr: List[int], element: int) -> List[int]:
    
    # create a shallow copy of arr
    arr_element_removed = arr.copy()

    # for every val that equals element, remove it
    
    for index, val in enumerate(arr_element_removed):
        if val == element:
            arr_element_removed.pop(index)
    return arr_element_removed




# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
