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

solution = Solution()
print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))
    