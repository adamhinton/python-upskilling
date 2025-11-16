from typing import List

def merge_sort(arr: List[int]):

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]

# Recursively:
    # Split array in half
        # Keep going until you get to just one item
    # Coming back up the recursion tree:
        # from left to right, compare a[left] to b[left] and so on
        # Add the lower item to solution first, then higher item
            # Or the other way around if it's descending order