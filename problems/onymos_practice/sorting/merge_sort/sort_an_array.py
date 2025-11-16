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

        def recursive_helper(nums: List[int]):
            if len(nums) > 1: # Base base, move back up tree if not
                left_arr = nums[:len(nums) // 2]
                right_arr = nums[len(nums) // 2:]

                recursive_helper(left_arr)
                recursive_helper(right_arr)

                # now both arrays are sorted

                i, j, k = 0, 0, 0 # left index, right index, nums index

                # Zip the two arrays in nums
                while (i < len(left_arr) and j < len(right_arr)):
                    left_el = left_arr[i]
                    right_el = right_arr[j]

                    if left_el <= right_el: # left is smaller or equal; stable sort
                        nums[k] = left_el
                        i += 1

                    else: # right is smaller or equal
                        nums[k] = right_el
                        j += 1
                    k +=1

                # Now deal with leftovers

                while i < len(left_arr):
                    left_el = left_arr[i]
                    nums[k] = left_el
                    i += 1
                    k += 1

                while j < len(right_arr):
                    right_el = right_arr[j]
                    nums[k] = right_el
                    j += 1
                    k += 1



        recursive_helper(nums)
        
        return nums
    
solution = Solution()
print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))
    
# PLAN
# Time complexity: O(n log(n))
# Space complexity: O(n) I think
# Need:
    # recursion
    # Merge sort

# PLAN:
# if len(nums) > 1: >> base case; when it's 1 start moving back up the tree
    # left_arr, right_arr = two halves of nums

    # merge_sort(left_arr)
    # merge_sort(right_arr)

    # Now both arrays are sorted. We combine them in nums, in place.

    # i = 0 >> left index
    # j = 0 >> right index
    # k = 0 >> nums index

    # Zip the two arrays in nums
    # while (i < len(left_arr) and j < len (right_arr)):

        # Stable sorting: if items are equal, left goes in first

        # left_el = left_arr[i]
        # right_el = right_arr[j]

        # if left_el < right_el:
            # arr[k] = left_el
            # i++

        # else: # they're equal or right is bigger
            # arr[k] = right_el
            # j++

        # k++
    
    # Now deal with leftovers

    # while i < len(left_arr):
        # left_el = left_arr[i]
        # nums[k] = left_el

    # while j < len(right_arr):
        # right_el = right_arr[j]
        # nums[k] = right_el
