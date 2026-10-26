from collections import Counter
from typing import Counter as CounterType

'''
counter = Counter(nums)  -> this will return the count of each occurrence without problem, even if we ask to count an element that does not exist

If we want to count another list in addition to the first in the same program we do:

counter.update(nums2) -> where nums2 is a separate list

'''

def count_chars(s1: str, s2: str) -> CounterType:

    # initializing first counter for s1_counter
    s1_counter = Counter(s1)
    # initializing the 2nd counter for each char occurrence in s2_counter
    s2_counter = Counter(s2)

    # adding the counts for each char together and storing it in s3_counter
    s3_counter = s1_counter + s2_counter

    return s3_counter


    
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
