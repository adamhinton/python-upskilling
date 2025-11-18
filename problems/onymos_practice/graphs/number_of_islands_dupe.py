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
from itertools import pairwiseπ

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        return num_islands