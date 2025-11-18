# 994. Rotting Oranges
# Medium
# https://leetcode.com/problems/rotting-oranges/description/

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

from typing import List, Tuple, Set
from enum import Enum

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        class Orange(Enum):
            NOT = 0
            FRESH = 1
            ROTTEN = 2

        rotting_orange_coords: Set[Tuple[int, int]] = set()
        num_fresh_oranges = 0
        num_minutes = 0
        m, n = len(grid), len(grid[0])
        DIRS = [(-1,0), (0,1), (1,0), (0,-1)]


        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == Orange.FRESH.value:
                    num_fresh_oranges += 1
                elif val == Orange.ROTTEN.value:
                    rotting_orange_coords.add((i, j))

        if num_fresh_oranges == 0: return 0

        if not bool(rotting_orange_coords): # no rottens to rot the fresh ones
            return -1
        
        # Stops if there are no rottens created after a round
        while(bool(rotting_orange_coords)):
            next_rotting_orange_set: Set[Tuple[int, int]] = set()
            num_minutes += 1
            for _, coords in enumerate(rotting_orange_coords):
                row, col = coords
                # Convert any orthogonally-adjacent freshes to rotten
                for a, b in DIRS:
                    x, y = row + a, col + b
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == Orange.FRESH.value:
                        # Convert to rotten
                        grid[x][y] = Orange.ROTTEN.value
                        num_fresh_oranges -= 1
                        next_rotting_orange_set.add((x, y))
            rotting_orange_coords = next_rotting_orange_set
            
        return num_minutes if num_fresh_oranges == 0 else -1


# PLAN
# Time: O(n)
# Memory: O(n)

# NEED:
    # BFS
    # Grid

# rotting_orange_coords: Set[Tuple[int, int]] = set()
# num_fresh_oranges = 0
# num_minutes = 0
# 
# Loop over grid elements:
    # if val == Orange.FRESH.value, num_fresh_oranges ++
    # elif val == Orange.ROTTEN.value, add coords to rotting_orange_coords

# if num_fresh_oranges == 0 return 0
# if there are no rotten oranges return -1

# while thare are elments in rotting_orange_coords AND >1 fresh oranges:
    # num_minutes += 1
    # for x, y in enumerate(rotten_orange_coords):
        # For each existing fresh orange orthogonal to these coords:
            # Set its value to Orange.ROTTEN.value (aka 2)
            # num_fresh_oranges --
            # add its coords to rotting_oranges_coords
        # remove (x, y) from rotting_oranges_coords 
            # because we've already rotten all the oranges next to it, don't need it anymore

# If there are fresh oranges left:
    # return -1
# else (all fresh oranges are now rotten):
    # return num_minutes
          

solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print(solution.orangesRotting([[0,2]])) # 0
