# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            
            # This is the only possible remaining case,
            # So could just be `else`
            # But I like the elif for clarity
            elif nums[mid] < target:
                low = mid + 1

            # This should never happen
            else:
                Exception("You suck!")
                
        return low
    
# Thoughts:
# Log(n) time (obviously)
# Binary search through sorted array

# PLAN:
# low and high pointers

# while low <= high:
    # mid = (high + low) // 2

    # if nums[mid] == target:
        # return mid -- happy path

    # if nums[mid] > target:
        # high = mid - 1

    # else if nums[mid] < target
        # low = mid + 1

# return low

# Not sure how to handle item not existing (TODO)

print(Solution().searchInsert([1,3,5,6], 5))  # → 2
print(Solution().searchInsert([1,3,5,6], 2))  # → 1
print(Solution().searchInsert([1,3,5,6], 7))  # → 4
print(Solution().searchInsert([1,3,5,6], 0))  # → 0