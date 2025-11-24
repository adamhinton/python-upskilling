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

from typing import List, Set, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(-1,0), (0,1), (1,0), (0,-1)]
        m, n = len(board), len(board[0])

        first_letter = word[0]
        path: Set[Tuple[int, int]] = set()

        def recursive_helper(row:int, col:int, index_needed) -> bool:
            if index_needed == len(word)-1: return True
            nonlocal path
            coords = (row, col)
            
            path.add(coords)

            next_needed_letter= word[index_needed + 1]
            
            for a, b in DIRS:
                x, y = row + a, col + b
                
                if ((0 <= x < m and 0 <= y < n ) 
                    and (board[x][y] == next_needed_letter)
                    and ((x, y) not in path)
                    ):
                    if recursive_helper(x, y, index_needed + 1): return True

            path.remove(coords)
            



        for row in range(m):
            for col in range(n):
                val = board[row][col]
                if val == first_letter:
                    if recursive_helper(row, col, index_needed=0): return True

        return False

# PLAN:
# Time: O(m * n * len(word)) - pretty nasty
# Space: O(n)
    # Could maybe make this O(1) by modifying board in place to denote that a square has been seen
    # like change it to "-1"
    # Then change back as we move up recursion tree
    # But that's overly complicated for a grid of less than 36 squares total

# Need:
    # Backtracking
    # Recursion
    # Hash sets of coords


# dirs = whatever
# m, n = len(board), len(board[0])
# first_letter = word[0]

# path = Set of (int, int) tuples 
    # Prevents dupes
    # Contains coordinates seen in current recursion tree
    # Remove coordinates as we move back up tree

# for row in range(m):
    # for col in range(n):
        # val = board[row][col]
        # if val == word[0]:
            # if recursive_helper(row, col, 0) return True

# def recursive_helper(row, col, index_needed):
    # if index_needed == len(word) -1:
        # return True

    # nonlocal path
    # path.add((row, col))

    # next_needed_letter = word[index_needed + 1]

    # for each orthogonal square, call recursive_helper(row, col, index_needed + 1) on it if:
        # square exists
        # square coords not in path
        # val == next_needed_letter

        # return True if any of these return True

    # path.remove(coords)


        




solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False
print(solution.exist([["a"]], "a")) # True