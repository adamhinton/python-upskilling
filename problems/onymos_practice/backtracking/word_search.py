# 79. Word Search
# https://leetcode.com/problems/word-search/description/

# Given an m x n grid of characters board and a string word, 
#   return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
#   where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

from typing import List
from itertools import pairwise

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return False


# PLAN:
# Time Complexity:
    # This one isn't pretty. Something like m * n * len(word)

# NEED:
    # Backtracking 
    # recursion
    # set for current path - set of coordinates to avoid repetition
        # will deconstruct the path as we move back up the recursion tree

# num_rows, num_columns = len(board), len(board[0])
# path = set()

# def recursive_helper(col, row, word_index_needed):
    # char_at_coords = board[row][column]
    # needed_char = word[i]

    # if i or j are out of bounds,
    # or if index >= len(word),
    # or if char_at_coords != needed_char:
        # return False
    
    # Now we know it's the next char we need

    # path.add((col, row))

    # For up down left right x, y:
        # recursive_helper(x, y, i+1)
    
    # path.remove((col, row))
