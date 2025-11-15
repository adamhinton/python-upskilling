# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

# Given an m x n 2D binary grid 
#   which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water 
#   and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# PLAN
# NEED: recursion, graph, DFS, BFS too I think?
# Time complexity: O(n) unless I'm much mistaken
    # Both the helper and the main loop will only touch each item once

# num_islands = 0

# Loop through each item
# WHen you first encounter a 1 in this main loop, islands++
#   If value == 1:
    # recursive_helper(current_coordinates)


# def recursive_helper(coordinates)
    # Not sure exactly what this should take in; coordinates maybe?

    # grid[coordinates] = 0

    # looping over the four potential neighbors:
        # If neighbor exists and has value 1:
            # recursive_helper(neighbor's coordinates)


# return num_islands

from typing import List
from itertools import pairwise

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
 
        def recursive_helper(i, j):
            grid[i][j] = 0

            for a,b in pairwise(dirs):
                x, y = i+a, j+b
                if (0<=x < m) and (0 <= y < n) and grid[x][y] == "1":
                    recursive_helper(x, y)

        # Outer loop

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == "1":
                    num_islands += 1
                    recursive_helper(i, j)


        return num_islands
    

solution = Solution()
print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1

solution = Solution()
print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3
    
