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

        tracker: Dict[int, int] = {}

        for idx, val in enumerate(nums):
            tracker[val] = idx
            needed = target - val
            if tracker.get(needed):
                return [tracker.get(needed), idx]

        raise ValueError("No solution found")
    
# PLAN:
# O(n)
# Need: hash table; Dict[int, int] : value, index
# Can do this in one pass I think. For every number, check if its needed num has already occurred
# Make tracker hash table
# for idx, num in enumerate nums:
    # tracker[num] = idx
    # needed = target - num
    # if needed in tracker, return [idx, index of needed]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # [0, 1]
print(solution.twoSum([3,2,4], 6)) #[1, 2]
print(solution.twoSum([3,3], 6)) #[0, 1]