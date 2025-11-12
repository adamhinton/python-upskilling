# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array
#    if you can flip at most k 0's.

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if (len(nums) == 1 or len(nums) == k): return len(nums)

        left, right = 0, 1
        running_zero_count = 0
        solution = 0

        while right < len(nums):
            right_val = nums[right]
            if right_val == 0:
                running_zero_count += 1

            while running_zero_count > k:
                left_val = nums[left]
                if left_val == 0: running_zero_count -= 1
                left += 1

            current_length = right - left + 1
            solution = max(current_length, solution)

        return 0
    
# PLAN:
# O(n)
# one pass

# Sliding window: Starting at length k
# if nums.length = k or 1 return nums.length
# left = 0
# right = k - 1
# running_zero_count = 0
# solution = 0

# enumerate over first k nums, running_zero_count++ for every 0
    # Actually maybe don't need this? Initialize k at 1?

# while right < len(nums):
    # right_val = nums[right]
    # if right_val == 0:
        # running_zero_count += 1

    # while running_zero_count > k:
        # if nums[left] == 0 running_zero_count --
        # left += 1

    # current_length = right - left + 1
    # solution = max(current_length, solution)

# return solution