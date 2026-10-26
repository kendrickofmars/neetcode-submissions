from typing import List
    # in python we can just use lists to immitate a stack
    # push (append), pop removes and returns top element from stack
    # in order to peek at the top element, we can just use -1
    # len(stack) to check if stack is empty
    # all operations are done in O(1)
def reverse_list(arr: List[int]) -> List[int]:
    # declare empty stack    
    stack = []
    # as long as stack is not empty pop elements and append them to new stack
    while len(arr) > 0:
        stack.append(arr.pop())
    return stack


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
