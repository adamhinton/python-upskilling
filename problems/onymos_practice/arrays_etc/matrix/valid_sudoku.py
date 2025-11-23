# 36. Valid Sudoku
# Medium
# Review later
# https://leetcode.com/problems/valid-sudoku/description/

# Determine if a 9 x 9 Sudoku board is valid. 
#   Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_tracker: Dict[int, Set[int]] = defaultdict(set) # rowindex: set of vals in row
        cols_tracker: Dict[int, Set[int]] = defaultdict(set) # colindex: set of vals in col
        subsquares_tracker: Dict[(int, int), Set[int]] = defaultdict(set) # (r// 3, c // 3): set of vals in col

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".": # Empty cell, all gucci
                    continue

                subsquare_coords = (row // 3, col // 3)

                if (
                    (val in rows_tracker[row]) 
                    or (val in cols_tracker[col]
                    or (val in subsquares_tracker[subsquare_coords])
                    )
                ):
                    return False
                
                rows_tracker[row].add(val)
                cols_tracker[col].add(val)
                subsquares_tracker[subsquare_coords].add(val)

        
        return True

# PLAN:

# Notes:
# Only filled cells must be validated. It doesn't matter if the board is unsolvable.
# If [3,2] must be a 9 because of its row and a 3 because of its column, that doesn’t matter.
# Values are STRINGS, not numbers
# Empty squares are "."

# Time: O(81) one pass
# space: O(1)
# need: Hash sets

# General idea:
    # Make a hash set for rows, hash set for cols and hash set for squares
    # For row and col hash sets, they're indexed by their index number  
        # e.g. row at index 3 is rows[3]
    # For squares, it's indexed by (row //3, col // 3)
        # e.g. [0, 1], [2, 2]
        # Value won't exceed 2
    # Each will have a set of numbers
        # If you arrive at a val and that val is already in its row/set/square's hash set, return False


solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # True

print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # False