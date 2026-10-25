from typing import List, Dict


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    # declare empty dictionary to append items to
    new_name_and_score_dict = {}

    # for name, score in zip(names, scores):
    #     new_name_and_score_dict[name]
    
    return dict(zip(names,scores))

# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
