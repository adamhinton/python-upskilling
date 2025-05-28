# https://leetcode.com/problems/two-sum/submissions/1647458201

# I'm about to start three sum
# So I'm doing two sum first to get the idea.

# Given an array of integers nums and an integer target, 
#   return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
#   and you may not use the same element twice.

# You can return the answer in any order.

from typing import List, Tuple, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        seen_numbers: Dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_numbers:
                return (i, seen_numbers[complement])
            
            seen_numbers[num] = i

        raise ValueError("No solution found")    

# PLAN

# value, index
# seen_numbers: Dict[int, int] = {}

# for i, num in enumerate(nums):
    # complement is target - num
    # if seen_numbers has needed num, return (i, seen_numbers[complement])

    # seen_numbers[num] = i