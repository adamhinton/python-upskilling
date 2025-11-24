# 733. Flood Fill
# Easy
# https://leetcode.com/problems/flood-fill/description/

# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original_color = image[sr][sc]
        if original_color == color: return image

        DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

        m, n = len(image), len(image[0])

        def recursive_helper(i, j):
            image[i][j] = color # this only gets called if the val is the color we need to change

            for a, b in DIRS:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and (image[x][y] == original_color):
                     recursive_helper(x, y)

        recursive_helper(sr, sc)

        return image
        
        

# PLAN
# Time: O(n)
# Space: O(n) I think)

# original_color = image[sr][sc]
# m, n = len(image), len(image[0])

# def recursive_helper(row, col):
    # image[row][col] = color >> this only gets called if it has the original color, so this is safe to changes

    # for coords in adjacent squares:
        # recursive_helper on coords if:
            # val == original color
            # square exists

# for row in range(m):
    # for col in range(n):
        # val = image[row][col]
        # if val == original_color:
            # recursive_helper(row, col)

# return image

solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))  #  [[2,2,2],[2,2,0],[2,0,1]]
