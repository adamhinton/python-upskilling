# Doing this again for practice

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


from typing import List, Set, Tuple
from itertools import pairwise

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def recursive_helper(row: int, col: int, curr_word_index: int):
            if curr_word_index == len(word):
                return True
            
            val = board[row][col]
            needed = word[curr_word_index]

            if needed == val:
                path.add((row, col)) # prevent dupe square checks

                for a,b in pairwise(dirs):
                    x, y = i+a, j+b
                    # square exists, has the val we're looking for, and square hasn't already been seen in this run
                    if (0<=x < m) and (0 <= y < n) and board[x][y] == word[curr_word_index + 1] and ((row, col) not in path):
                        if recursive_helper(x, y): return True 

                path.remove((row, col))
            
            # return False



        m, n = len(board), len(board[0])
        path: Set[Tuple[int, int]] = set() # seen coords
        # curr_word_index = 0
        dirs = (-1, 0, 1, 0, -1)

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                needed = word[0]
                if val == needed:
                    if recursive_helper(i, j, 0) is True: return True

    


        return False

# PLAN:
# Time: Something nasty; O(n * m * len(word)) or something like that
# Space: O(n)
# NEED:
    # Set; path of tuples -- the seen coordinates for the current run
        # Coordinates get removed as you go back up the recursion tree
    # Recursion
    # Backtracking
    #DFS

# m = len(board)
# n = len(board[0])
# path: Set[Tuple[int, int]] = set() # current seen coordinates

# for i in range(m):
    # for j in range(n):
        # val = board[i][j]
        # needed = word[0]
        # if val == needed:
            # if recursive_helper(i, j, 0) return True

# def recursive_helper(row: int, col: int, curr_word_index: int):
    # if curr_word_index == len(word): # word complete
        # return True

    # val = board[row][col]

    # needed = word[curr_word_index]

    # if needed == val:
        # seen.add((row, col))
        # call recursive_helper for squares orthogonal from the current square with curr_word_index++, if:
            # 1. They exist
            # 2. Their coordinates aren't already in `seen`
        # return True if any of the above are True; False if not


# return False, all possibilities exhausted


solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False