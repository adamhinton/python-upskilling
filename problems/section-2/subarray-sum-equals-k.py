# Given an array of integers nums and an integer k, 
#   return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return 0
    

print(Solution().subarraySum(nums = [1,1,1], k = 2)) # 2
print(Solution().subarraySum(nums = [1,2,3], k = 3)) # 2
