# 55. Jump Game
# Medium
# https://leetcode.com/problems/jump-game/description/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # last index
        for i in range(goal, -1, -1):
            val = nums[i]
            needed_steps = goal - i
            if val >= needed_steps:
                goal = i
        
        return goal == 0

        
    
solution = Solution()
print(solution.canJump([2,3,1,1,4])) # True
print(solution.canJump([3,2,1,0,4])) # False

# PLAN
# Time: O(n)
# Space: O(1)
# Need:
    # Greedy
    # I think that's all

# Idea: Moving the goalposts
# If we can get to square at index i, we can get to any square before it.
# So we start with the goal at nums[len(nums) -1]
    # Then, loop backwards over index i
    # if nums[i]'s val is high enough to jump to goal,
        # goal = i

# return goal == 0 >>> We've gotten to the front. Yay!

# Possible optimizations:
    # None immediately come to mind
