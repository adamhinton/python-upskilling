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
from itertools import pairwise

class Solution:
    def solve(self, board: List[List[Literal['X', 'O']]]) -> None:
        return None
    

# PLAN:
# Time complexity: 
    # A lot. m * n * ... the average length of regions I think

# Need:
# Backracking
# DFS

# num_rows, num_cols
# dirs = (-1, 0, 1, 0, -1)
# seen = set() >>> tuples of (row, col)
    # the coords the recursive function has visited 
    # I *think* that if it has already been seen by the inner loop, we don't need to check it again
    # So coords are added to `seen` and never removed



# def recursive_helper(row, col, is_valid_region_for_surround) -> bool:
    # If true and all deeper recursive calls are true, modify square
        # Always call all squares, don't return early
        # Always add coords to seen (which is why we don't return early)

    # I decided to check in the function whether it's a valid square, as opposed to outside the fn
    # current_value = board[row][col]

    # If any is true, don't modify square; but continue recursing to add all squares in the region to seen:
        # touches_edge == True
        #  

# for i in range (num_rows):
#   for j in range(num_cols):
        # current_val = board[i][j]

        # if coords in seen:
            # skip

#       touches_edge = False

        # if has edge neighbors:
            # touches_edge = True

#       # dfs(i, j)

        # 

