# Doing this again for review

# 15. 3Sum
# Medium

# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []

        return solution


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
# [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1]))
# []
print(solution.threeSum([0,0,0]))
# [[0, 0, 0]]
