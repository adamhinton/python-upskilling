# 130. Surrounded Regions

# https://leetcode.com/problems/surrounded-regions/description/

# You are given an m x n matrix board containing letters 'X' and 'O', 
#   capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells 
#   if you can connect the region with 'X' cells 
#   and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

from typing import List, Literal

class Solution:
    def solve(self, board: List[List[Literal['X', 'O']]]) -> None:
        return None
    

# PLAN:
# Time complexity: 
    # A lot. m * n * ... the average length of regions I think

# Need:
# Backracking
# DFS
