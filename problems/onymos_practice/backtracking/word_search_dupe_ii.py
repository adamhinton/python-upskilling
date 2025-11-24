# Doing this again (again) for practice

# 79. Word Search
# https://leetcode.com/problems/word-search/description/

# Given an m x n grid of characters board and a string word, 
#   return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
#   where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        return False



solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False
print(solution.exist([["a"]], "a")) # True