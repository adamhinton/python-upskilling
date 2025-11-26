# Doing this again for practice

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

    # solution = []
    # current_subset = []


# def recursive_helper(current_index: int):
    # nonlocal current_subset

    # if current_index == len(nums):
        # solution.append(current_subset)
        # return
    # current_subset.append(nums[i])
    # recursive_helper(current_index + 1)
    # current_subset.pop()
    # recursive_helper(current_index + 1)

solution = Solution()
print(solution.subsets([1,2,3]))