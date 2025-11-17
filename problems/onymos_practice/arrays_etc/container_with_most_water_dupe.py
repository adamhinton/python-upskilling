# Doing this again for practice
# 11. Container With Most Water
# Difficulty: Medium

# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            left_height, right_height = height[left], height[right]

            current_area = (min(left_height, right_height)) * (right - left)

            max_area = max(current_area, max_area)

            if left_height < right_height:
                left+=1

            else: # equal or less
                right -=1

        return max_area

# PLAN
# Time: O(n), one pass
# Space: O(1)
# Need: two pointers, shrinking window

# max_area = 0

# left, right = 0, len(height) - 1

# while left < right:
    # get current_area, left_height, right_height
        # the min of the two heights * (right - left)
    # max_area = max(max_area, current_area)
    # if left_height < right_height, left++
        # else right--

# return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(solution.maxArea([1,1])) # 1