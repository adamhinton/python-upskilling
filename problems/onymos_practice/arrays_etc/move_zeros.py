# 283. Move Zeroes
# Easy
# REVIEW LATER
# https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it 
#   while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        
solution = Solution()
# print(solution.moveZeroes([0,1,0,3,12])) # [1, 2, 12, 0, 0]
# print(solution.moveZeroes([0])) # [0]
# print(solution.moveZeroes([0, 1, 0])) # [1, 0, 0]
print(solution.moveZeroes([-58305,-22022,0,0,0,0,0,-76070,42820,48119,0,95708,-91393,60044,0,-34562,0,-88974]))