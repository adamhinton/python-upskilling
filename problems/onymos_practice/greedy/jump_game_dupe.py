# Doing this again for practice

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

        current = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            num = nums[i]
            needed_jump = current - i

            if num >= needed_jump:
                current = i
        
        return current == 0 # made it to the front    


solution = Solution()
print(solution.canJump([2,3,1,1,4])) # True
print(solution.canJump([3,2,1,0,4])) # False

# PLAN:
# Greedy
# O(n) memory, O(1) space

# Loop backwards over the array
# Track a `current` variable
# If the current num can reach `current`, current = i
# After loop, return current == 0

# current = len(nums) - 1
