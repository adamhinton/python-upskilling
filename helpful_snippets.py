# Get pairwise tuples of four directions
from itertools import pairwise
dirs = (-1, 0, 1, 0, -1)
for a,b in pairwise(dirs):
    pass 
# This will be: 
# : up (-1, 0), right (0, 1), down (1, 0), and left (0, -1).

    # for a,b in pairwise(dirs):
    #     x, y = i+a, j+b
    #     if (0<=x <= m) and (0 <= y <= n) and grid[x][y] == "1":
    #         recursive_helper(x, y)

            
# Stuff to try:
    # work backwards
        # start from right of array
        # Eliminate ineligible contenders first instead of finding eligible ones
            # e.g. in surroudned regions, eliminate ones who aren't surrounded first
    
    # modify arrays in place for tracking

    