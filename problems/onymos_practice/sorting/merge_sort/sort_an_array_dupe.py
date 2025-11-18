# Doing this again for practice
# 912. Sort an Array
# Medium
# https://leetcode.com/problems/sort-an-array/description/?envType=problem-list-v2&envId=merge-sort

# Given an array of integers nums, 
# sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions
#   in O(nlog(n)) time complexity 
#   and with the smallest space complexity possible.

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def recursive_helper(nums):
            total_nums = len(nums)

            if total_nums > 1: # base case, if 1 move up tree
                left_nums = nums[:total_nums//2]
                right_nums = nums[total_nums//2:]

                recursive_helper(left_nums)
                recursive_helper(right_nums)

                # Now the arrays are sorted

                # k is index in nums
                left_index, right_index, k = 0, 0, 0 

                while left_index < len(left_nums) and right_index < len(right_nums):
                    if left_nums[left_index] <= left_nums[right_index]:
                        nums[k] = left_nums[left_index]
                        left_index += 1
                        k += 1

                    else: # right val is strictly less
                        nums[k] = right_nums[right_index]
                        right_index += 1
                        k += 1

                    while left_index < len(left_nums):
                        nums[k] = left_nums[left_index]
                        left_index += 1
                        k += 1
                    
                    while right_index < len(right_nums):
                        nums[k] = right_nums[right_index]
                        right_index += 1
                        k += 1

        recursive_helper(nums)

        return nums


solution = Solution()
print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))
    
# PLAN:
# Time: O(n log n)
# Space: O(n) I think

# total_nums = len(nums)

# if total_nums > 1: >>> base case: just move up recursion tree if 1
    # left_nums = nums[:total_nums//2]
    # right_nums = nums[total_nums//2:]

    # sortArray(left)
    # sortArray(right)

    # Now the arrays are sorted

    # left_index = 0
    # right_ index = 0
    # k = 0 # nums index

    # while left index is less than left_nums length and right index is less than right nums length:

        # if left_val <= right_val: Preserve stable sort
            # nums[k] = left_val
            # left_index++
            # k++
        
        # if right_val < left_val:
            # nums[k] = right_val
            # right_index++
            # k++

        # while left_index < len(left_nums):
            # nums[k] = left_val
            # left++
            # k++

        # while right_index < len(right_nums):
            # nums[k] = right_val
            # right++
            # k++
 