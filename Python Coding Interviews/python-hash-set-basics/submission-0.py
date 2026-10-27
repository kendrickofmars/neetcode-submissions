from typing import List, Set

'''
hashsets can't contain duplicates, all operations done in O(1) time. They only store the keys, not keys + values.
insertion:
hash_set() = set()
hash_set.add('a') # {'a'}
deletion:
hash_set.remove('a') # raises keyerror if key not in set
hash_set.discard('b') # doesn't raise keyerror if key not in set
lookup:
'a' in hash_set # True
'''

def build_hash_set(keys: List[str]) -> Set[str]:
    # this hashset will hold the list of keys
    hash_set = set()
    # looping through our list of keys O(n)
    for key in keys:
        hash_set.add(key)
    

    return hash_set


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    #O(1) operation to perform a lookup on a hash_set
    # creating a list to hold each result from the key-lookup operation
    key_in_hash_set = []

    for key in keys:
        # appending the boolean value returned from every lookup 
        key_in_hash_set.append(key in hash_set)

    return key_in_hash_set


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
