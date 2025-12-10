# Doing this again for practice

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        return nums


solution = Solution()
print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))

# PLAN:
# def recursive_helper(nums):
# if nums.length is 1, return

# Divide nums in to left_nums and right_nums of ~equal length
# recursive_helper on left nums and right nums >>> now we know they're sorted or length 1

# i = 0 >> index in nums_left
# j = 0 >> index in nums_right
# k = 0 # index in master nums

# while i and j are less than the lengths of their respective arrays:
    # left_num = left_nums[i]
    # right_num = right_nums[nums_right_ind]

    # if left_num <= right_num: left is less than or equal
        # nums[k] = left_num
        # i ++
        # k ++

    # else >> right is strictly greater
        # nums[k] = right_num
        # j++ 
        # k++

# while i < len(nums_left):
    # num = nums_left[i]
    # nums[k] = i
    # k++, i++


# while j < len(nums_right):
    # num = nums_right[j]
    # nums[k] = j
    # k++, j++





# recursive_helper(nums)
# return nums