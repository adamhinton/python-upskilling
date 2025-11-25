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
    def threeSum(self, nums:  List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums]
        solution = []

        return solution
    
# PLAN:
# time: O(n ** 2)
# Space: O(n)
# Need:
    # Sorting
    # Two pointers (start and end)

# Sort nums
# solution = []

# For idx in range(len(nums) -2): >>> stop when less than three nums left
    # if previous num == num, continue >>> avoid dupes
    # If num > 0: break

    # left, right = idx + 1, len(nums) - 1

    # while right > left and right val isn't a negative number:
        # needed = 0 - num
        # if right val + left val == needed: solution.append([num, left, right])
        # If it's less than needed, left ++
            # Keep doing this until we get a new left val, no dupes
        # else it's more than needed, right--
            # keep doing this until we get a new right val, no dupes

    # return solution


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
# [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1]))
# []
print(solution.threeSum([0,0,0]))
# [[0, 0, 0]]
