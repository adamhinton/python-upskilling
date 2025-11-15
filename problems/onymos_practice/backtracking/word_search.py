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
        num_rows, num_columns = len(board), len(board[0])
        path = set()
        dirs = (-1, 0, 1, 0, -1)
        # pairwise_dirs = pairwise(dirs)

        def recursive_helper(row: int, col: int, word_index_needed: int):
            if word_index_needed == len(word): # The word has been completed
                return True

            if (row < 0 or row >= num_rows) or (col < 0 or col >= num_columns) or board[row][col] != word[word_index_needed] or (row, col) in path:
                return False
            
            char_at_coords = board[row][col]
            char_needed = word[word_index_needed]
            
            # Now we know it's the char we need

            
            path.add((row, col))

            for a,b in [(-1,0), (0,1), (1,0), (0,-1)]:
                if recursive_helper(row + a, col + b, word_index_needed + 1):
                    return True
            

            path.remove((row, col))

            return False
        
        for i in range (num_rows):
            for j in range( num_columns):
                current_letter = board[i][j]
                if current_letter != word[0]:
                    continue
                if recursive_helper(i, j, 0):
                    return True
                
        return False


# PLAN:
# Tcolme Complexity:
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
        # if recursive_helper(x, y, i+1):
            # return True
    
    # path.remove((col, row))

    # Now it moves on to the next letter in the outer loop

solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False