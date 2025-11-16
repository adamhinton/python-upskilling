# 78. Subsets
# https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []

        
        
        return solution
    
# PLAN:

# NEED:
    # Backtracking
    # Recursion

# Time complexity:
    # a lot
    # 2 ^ n I think

# total_nums = len(nums)

# solution = []
# running_list = []


# def recursive_helper(i: int):
    # If end of nums, 
    #   solution.append(running_list[:])
    #   return

    # current_val = nums[i]

    # First, recurse without adding nums[i]
    # recursive_helper(i+1)

    # Then, add nums[i] and recurse:
        # sol.append(current_val)
        # recursive_helper(i+1)
        # sol.pop()