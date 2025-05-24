# https://www.codewars.com/kata/6355535de93f4f003d68daaa

# Instructions:
# This is a classic FAANG problem
# Takes in list of positive integers
# Each int represents the height of a column in the x (horizontal) position i.
# Find two columns, which together with the x-axis form a container, 
    # such that the container contains the most water.
# Return an integer - the MAX AREA of water that can be contained

# Thoughts:
# Sliding unfixed window
# I belive I can make this O(n)

from typing import List

def maxContainerWater(height: List[int]) -> int:

    if len(height) == 0:
        return 0

    max_area = 0
    left, right = 0, len(height) - 1

    while right > left:
        left_height = height[left]
        right_height = height[right]

        current_area = (right - left) * min(left_height, right_height)
        max_area = max(current_area, max_area)

        if left_height < right_height:
            left += 1

        else:
            right -= 1


    return max_area

print(maxContainerWater([1,8,6,2,5,4,8,3,7])) # 49
print(maxContainerWater([1, 5, 6, 3, 4, 2])) # 12
print(maxContainerWater([1])) #0
print(maxContainerWater([1,1])) # 1

# PLAN:
# maxArea = 0
# left, right = 0, len(height) - 1

# while right > left:
    # left_height = height[left]
    # right_height = height[right]

    # current_area is (right - left) * min (height[left], height[right])
    # max_area is now the greater of max_area and current_area

    # if left_height < right_height left++; else right--

# return max_area

# I feel like I'm missing some step but we'll give this a shot.