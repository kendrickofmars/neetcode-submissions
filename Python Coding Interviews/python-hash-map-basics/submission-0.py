from typing import List, Dict
'''
use dictionaries to implement hashmaps e.g.
hashmap = {}
insert into hashmap O(1)
hashmap['a'] = 1 # {'a': 1}

access O(1)
print(hashmap['a']) # access via key 'a', return value '1'

deletion is O(1), and pops a key-value pair from the hashmap
del hashmap['a'] 
or use 'pop', which functions similarly to del, but returns value as well
hashmap.pop('a')

Lookup O(1), checking if value exists in hashmap, just use keyword 'in', return boolean
does_a_exist = 'a' in hashmap # return True
does_b_exist = 'b' in hashmap # return False

'''

def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    # declare an empty dictionary aka hashmap
    hash_map = {}
    # zip keys and values together
    for key, value in zip(keys, values):
        hash_map[key] = value
    # returning the resultant hash_map 
    return hash_map 


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    # create an empty list to hold the integer values to return, given names as the key
    scores = []

    # loop through the key in keys to be used to access the values in hash_map
    for key in keys:
        scores.append(hash_map[key])
    return scores



# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
