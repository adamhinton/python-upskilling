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
        

# PLAN
# Time: O(n)
# Space: O(n) I think)

# original_color = image[sr][sc]
# m, n = len(image), len(image[0])

# def recursive_helper(row, col):
    # val = image[row][col]
    # if val == original_color:
        # image[row][col] = color

    # for existing coords in adjacent squares:
        # recursive_helper on coords if:
            # val == original color
            # square exists

# for row in range(m):
    # for col in range(n):
        # val = image[row][col]
        # if val == original_color:
            # recursive_helper(row, col)

solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
