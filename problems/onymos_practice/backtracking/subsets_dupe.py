# Doing this again for practice

# 78. Subsets
# https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        current_subset = []

        def recursive_helper(current_index: int):
            nonlocal current_subset
            if current_index == len(nums):
                solution.append(current_subset.copy())
                return
            
            # Path 1: Add current number
            current_subset.append(nums[current_index])
            recursive_helper(current_index + 1)

            # Path 2: Don't add current number
            current_subset.pop()
            recursive_helper(current_index + 1)

        recursive_helper(0)
        return solution

# solution = []
# current_subset = []


# def recursive_helper(current_index: int):
    # nonlocal current_subset

    # if current_index == len(nums):
        # solution.append(current_subset)
        # return
    # current_subset.append(nums[i])
    # recursive_helper(current_index + 1)
    # current_subset.pop()
    # recursive_helper(current_index + 1)

# return solution

solution = Solution()
print(solution.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(solution.subsets([0])) # [[], [0]]