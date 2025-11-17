# 15. 3Sum
# Medium

# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import Tuple, List

class Solution:
    def threeSum(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        solution = []

        nums.sort()
        total_nums = len(nums)

        for i in range(total_nums - 2):
            val = nums[i]
            if val > 0:
                break

            left = 0
            right = total_nums - 1

            while left < right:
                num_j = nums[left]
                num_k = nums[right]

                needed = 0 - val

                if needed < val:
                    break

                j_plus_k = num_j + num_k

                if j_plus_k == needed:
                    solution.append((val, num_j, num_k))
                    # Should I be incrementing both of these?
                    left += 1
                    right -= 1
                    continue

                if j_plus_k < needed:
                    left += 1
                    continue

                if j_plus_k > needed:
                    right -= 1
                    continue
                
                else:
                    ValueError("This should never happen, you dummy!")
        return solution
    

# PLAN
# Time: O(n^2)
# Space: O(n) I believe
# Need: Two pointers, sorting
    # Don't think I need a hash map
# Note: I'm returning tuples of values, not tuples of indexes
    # I think some variations of this want tuples of indexes

# arr.sort()
# total_nums = len(nums)

# for i in range(total_nums - 2): >> stop two nums before end of array
    # val = nums[i]

    # left = 0
    # right = total_nums - 1

    # while left < right:
        # num_j = nums[left]
        # num_k = nums[right]

        # needed = 0 - val

        # j_plus_k = num_j + num_k

        # IF j_plus_k == needed:
            # solution.append((val, num_j, num_k))
            # left++ 
            # right--
            # continue

        # if j_plus_k < needed:
            # left++
            # continue

        # else: >> j_plus_k is greater than needed
            # right--
            # continue


# return solution


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
# [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1]))
# []
print(solution.threeSum([0,0,0]))
# [[0, 0, 0]]
