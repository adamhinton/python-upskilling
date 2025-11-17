# Doing this again for practice
# Medium
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        running_num_zeros = 0

        if len(nums) == 1:
            return 0 if (k == 0 and nums[0] == 0) else 1
        
        left, right = 0, 1
        
        if nums[left] == 0: 
            running_num_zeros += 1 # we'll deal with nums[right] inside the loop

        while right < len(nums):
            num_left, num_right = nums[left], nums[right]

            if num_right == 0:
                running_num_zeros += 1

            while running_num_zeros > k:
                if num_left == 0:
                    running_num_zeros -= 1
                left+=1
                num_left = nums[left]

            # Now we know it's a valid window
            current_length = right - left + 1
            max_length = max(current_length, max_length)
            right +=1

        return max_length




        
        


        return max_length
    
# PLAN:
# Time complexity: O(n), one pass
# Space comp: O(1) I believe

# Need:
# Two pointers, start at index 0 and 1

# running_num_zeros = 0
# left, right = 0, 1
# if nums[left] == 0, running_num_zeros ++

# Sliding window pattern:
    # while right < len(nums) >>> don't think it would help to do like `and left < len(nums) - k`
        # if nums_right] == 0, running_num_zeros++

        # Don't believe we need to make sure left never equals right
        # window between nums left and nums right 
        # While there are too many zeros (aka we can't flip them all):
            # if nums[left] == 0, decrement running_num_zeros
            # incrememt left

    # Now we know it's a valid window
    # max_length = max(right - left, max_length)
    # right++

    
solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k=2)) # 6
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3)) # 10