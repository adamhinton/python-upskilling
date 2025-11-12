# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

from typing import List, Dict
import math

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker: Dict[int, int] = {
        } # val, index
        next_index = -1
        # highest_seen_number = -math.inf

        for idx, num in enumerate(nums):
            if tracker.get(num) is None:
                next_index += 1
                nums[next_index] = num
                tracker[num] = idx
                # highest_seen_number= num

        return next_index + 1
    

solution = Solution()
print(solution.removeDuplicates([1, 1, 2])) # 2
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
                 
        

# PLAN:
# Hash table `tracker` to store first seen index of a number
# O(n)
# highest_seen_number = -infinity
# When we find a new highest number, set it to the index above the previous highest seen num
    # This means we don't need a second pass thru
# for idx, num in enumerate(nums):
    # if num not in tracker:
        # next_index = tracker.get(highest_seen_num) + 1
        # nums[next_index] = num
        # tracker[num] = idx
    # else:
        # first_index = tracker[num]
