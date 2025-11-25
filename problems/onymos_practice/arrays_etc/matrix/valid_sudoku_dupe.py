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

from collections import List
from typing import Tuple, DefaultDict, Set

# Doing this horror show more for comedy than anything
# I miss TypeScript
Row = Tuple[str, str, str, str, str, str, str, str, str]
Board = Tuple[
    Row, Row, Row, Row, Row, Row, Row, Row, Row
]

class Solution:
    def isValidSudoku(self, board: Board) -> bool:

        return True
    
# PLAN
# Time: O(n) one pass
# Space: O(n) just need sets of coords
# Time and space would increase linearly if you added more rows/cols

# Make three dicts. 
    # row_tracker: 
    #   Key: row_index (0-8)
    #   val: set of strings contained in row

    # col_tracker: 
    #   Key: col_index (0-8)
    #   val: set of strings contained in col

    # subsquare_tracker:
        # key: (row//3, col//3) 
        #   each coord will be 0, 1 or 2
        # val: set of strings contained in subsquare

    
    # for row, col etc:
        # if val is "." continue
        # if val in row_tracker[row]: return False
        # if val in col_tracker[col]: return False
        # if val in subsquare_tracker[(row//3, col//3)]: return False

        # add val to row tracker, col tracker and subsquare tracker

# return True



# Constraints:
    # All inputs will be valid; no integers instead of strings etc

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