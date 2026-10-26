from typing import List

# O(1) time
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    # for every element in arr2, append it to the end of arr1
    for i in arr2:
        arr1.append(i)
    # return new arr1
    return arr1

# O(1) time
def pop_n(arr: List[int], n: int) -> List[int]:
    while n > 0 and arr:
        arr.pop()
        n -= 1
    return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    # if oob insert element at end
    if index < 0 or index >= len(arr):
        arr.append(element)
    else:
        arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
