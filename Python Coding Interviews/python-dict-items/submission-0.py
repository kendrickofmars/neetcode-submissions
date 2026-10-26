from typing import Dict, List, Tuple


'''
we can access the just the keys/values without having to loop over the entire dictionary by using:
dict.keys() and dict.values(). Both methods return view objects, which we can convert to lists like so: 
keys_list = list(keys)

to get key-value pairs we can simply do this:
for key, value in dict.items():
    print(key, value)
'''

def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    
    # syntax to instantiate a list to hold our tuple of key-value pairs
    names_and_ages = []


    # loop through using unpacking of age_dict items and add it to 
    for name, age in age_dict.items():
        # append the values as a tuple, since append only takes in 1 arg
        names_and_ages.append((name,age))
    return names_and_ages


# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
