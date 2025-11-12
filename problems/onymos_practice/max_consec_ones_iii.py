# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array
#    if you can flip at most k 0's.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        return 0