# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/description/

# You are given an image represented by an m x n grid of integers image, 
#   where image[i][j] represents the pixel value of the image. 
# You are also given three integers sr, sc, and color.
#  Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent 
#   (pixels that share a side with the original pixel,either horizontally or vertically) 
#   and shares the same color as the starting pixel.

# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

from typing import List
from itertools import pairwise

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        new_color = color # I like this naming better
        if original_color == new_color: return image
        dirs = (-1, 0, 1, 0, -1) # will use this to make directional changes

        m, n = len(image), len(image[0])


        def recursive_helper(i: int, j: int):
            image[i][j] = new_color

            for a, b in pairwise(dirs):
                x, y = i + a, j+ b

                if (0 <= x < m) and (0 <= y < n) and (image[x][y]== original_color):
                    recursive_helper(x, y)

        recursive_helper(sr, sc)

        return image

solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

# PLAN
# O(n)
# DFS
# Graph
# Recursion

# original_color = image[sr][sc]
# new_color = color >>> less confusing naming

# Start at specified coordinates. 

# def recursive_helper(i, j):
    # image[i][j] = new_color
    # for pixel in up down left right (if they exist):
        # if pixel color == original color, recursive_helper(pixel's coordinates)

# Starting at original coordinates:
    # recursive_helper(sr, sc)

# return image
