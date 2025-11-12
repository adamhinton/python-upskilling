# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. 
# There are n vertical lines drawn
#    such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        best_area = 0
        left = 0
        right = len(height) - 1

        while left< right:
            l_height = height[left]
            r_height = height[right]
            curr_length = right - left
            curr_best_height = min(l_height, r_height)
            current_area = curr_length * curr_best_height
            best_area = max(current_area, best_area)

            if l_height < r_height:
                l += 1
            else:
                right-= 1

        return best_area
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(solution.maxArea([1, 1])) # 1

    

# PLAN:
# Need:
# sliding window - start at 0 and 1
# Calculate area for each configuration

# best_area = 0
# left = 0
# right = 1
# best_left_index = 0

# loop through:
# Calculate current area - length (right - left - 1) * height (min(height[left], height[right]))
# If that's better than best area, best_left_index = left 
# right++

