# 88. Merge Sorted Array
# Easy

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function,
#  but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m - 1, n - 1
        write_index = m + n -1

        while j >= 0: # if j has run out, all remaining elements in n1 are smaller than all elements in n2
            val1 = nums1[i]
            val2 = nums2[j]

            if i >= 0 and val1 > val2:
                nums1[write_index] = val1
                i -= 1

            else: # val2 is greater or equal
                nums1[write_index] = val2
                j-= 1

            write_index -= 1




solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)) # [1, 2, 2, 3, 5, 6]