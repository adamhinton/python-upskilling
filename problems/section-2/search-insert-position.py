# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return 0
    
# Thoughts:
# Log(n) time (obviously)
# Binary search through sorted array

# PLAN:
# left and right pointers

# while low < high:
    # mid = (high + low) // 2

    # if nums[mid] == target:
        # return mid -- happy path

    # if nums[mid] > target:
        # right = mid - 1

    # else if nums[mid] < target and nums[mid + 1] <= target:
        # left = mid + 1

    # I think this means target is between nums[mid] and nums[mid + 1]
    # else:
        # Return mid + 1

# Not sure how to handle item not existing (TODO)
