# 1020. Number of Enclaves
# Medium
# https://leetcode.com/problems/number-of-enclaves/description/

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        num_enclaves = 0

        m, n = len(grid), len(grid[0])

        DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

        def recursive_helper(row, col):
            # val = grid[row][col]
            # if val == 0: return # maybe do this before calling

            grid[row][col] = 0

            is_border_square = (row == 0 or col == 0 or row == m-1 or col == n-1)

            if is_border_square: is_enclave = False

            for a, b in DIRS:
                x, y = row + a, col + b
                if (0 <= x < m and 0 <= y < n) and grid[x][y] == 1:
                    recursive_helper(x, y)




        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == 0: continue

                # now we know it's land
                is_enclave = True # helper will set this to false if it finds a border square
                recursive_helper(i, j)

                if is_enclave == True: num_enclaves += 1



        return num_enclaves
    
    
# PLAN
# Time: O(m * n * ... length of average island, I think)
# space: O(n)
# Need:
    # Recursion
    # backtracking
    # `seen` set for current path coordinates
    # DFS

# m, n = len(grid), len(grid[0])
# num_enclaves = 0

# def recursive_helper(row, col):
    # val = grid[row][col]
    # if val == 0: return >> or check for this before calling recursive_helper
    # if it's a border square, is_enclave = False
    
    # for each adjacent square:
        # call recursive_helper(adjacentcoords) if:
            # square exists, and
            # maybe check here whether its val is 0?


# for i, j in whatever:
    # if val is 1:
        # is_enclave = True >> recursive helper will change this if it finds a border square with val 1

        # recursive_helper(i, j)
            # set is_enclave to false if it's border square
            # set val to 0
            # call itself on adjacent squares
            # remove its coords from seen when done

        # if is_enclave num_enclaves ++

# return num_enclaves


solution = Solution()
print(solution.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])) # 3
print(solution.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])) # 0
