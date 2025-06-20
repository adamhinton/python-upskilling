from typing import List

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array 
#   if you can flip at most k 0's.

#https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        num_zeros = 0
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0: num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -=1
                left +=1

            max_len = max(max_len, right - left +1)

        return max_len

# PLAN
# Two pointers sliding window
    # Unfixed length
# Should be O(n)

# num_zeros = 0
# left = 0
# max_len = 0

# for right in range(len(nums)):

    # if nums[right] == 0 num_zeros ++
    
    # while num_zeros > k:
        # if nums[left] == 0 num_zeros --
        # left += 1

    # Not sure if the + 1 is needed here
    # max_len = max (max_len, (right - left + 1))

# return max_len