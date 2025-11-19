# 1020. Number of Enclaves
# Medium
# https://leetcode.com/problems/number-of-enclaves/description/

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        num_enclaves = 0
        return num_enclaves