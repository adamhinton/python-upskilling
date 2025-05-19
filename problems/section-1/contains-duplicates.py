# https://www.codewars.com/kata/5558cc216a7a231ac9000022/train/python

from typing import Dict, List, Any, Tuple  # noqa: F401

# Plan:
# solution = []
# dupe_check = {}

# Loop through array (obviously)

# Note, We just add items to the solution in the order that we spot they're duplicates.

# Gotta make sure we only add duplicates to solution once. 

# UPDATE: This plan didn't survive first contact. Leaving it for posterity.
# for item in arr:
    ## If not dupe_check[item]:
        ### dupe_check[item] = 1

    ## else if dupe_check[item] == 1:
        ### solution.append(item)

    ## dupe_check[item] +=1

    ## return solution        

def duplicates(arr: List[Any]) -> List[Any]:
    solution = []
    seen = {}

    for item in arr:
        count = seen.get(item, 0)

        if count == 1:
            solution.append(item)
        
        seen[item] = count + 1

    return solution

print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'])) # [4, 3, 1]