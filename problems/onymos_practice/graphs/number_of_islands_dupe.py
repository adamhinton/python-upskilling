# Doing this again for practice

# 200. Number of Islands
# Medium
# https://leetcode.com/problems/number-of-islands/description/

# Given an m x n 2D binary grid 
#   which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water 
#   and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

from typing import List
from itertools import pairwise

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        return num_islands
    
# PLAN:
    # Time: Something nasty, m * n * average length of islands I think
    # Space: O(1)

    # Broad plan:
        # for each item, if it is 1,
            # Change it to 0, num_islands ++
            # for each square up, left, down, right (if they exist)
                # call recursive helper(row, col) 
        
        # recursive helper(row, col):
                # This sets a square's value to 0, then searches for more connecting land and sets those to 0 too.
                # Should recurse all the way through an island then stop.
                # Converts land from 1 to 0 so it doesn't get visited again.
            # if val is 0, return
            # if val == 1:
                # change val to 0
                # for each orthogonal square (that exist):
                    # recursive helper on that orthogonal square

# num_islands = 0




# return num_islands