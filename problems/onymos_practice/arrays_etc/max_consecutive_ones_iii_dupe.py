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

        return max_length
    
# PLAN:
# Time complexity: O(n), one pass
# Space comp: O(1) I believe

# Need:
# Two pointers, start at index 0 and 1

    
solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k=2)) # 6
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3)) # 10