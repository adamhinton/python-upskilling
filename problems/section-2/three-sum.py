# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, 
#   return all the triplets [nums[i], nums[j], nums[k]] 
#   such that i != j, i != k, and j != k, 
#   and nums[i] + nums[j] + nums[k] == 0.

# Notice that the order of the output 
#   and the order of the triplets does not matter.

# PLAN:
# We'll need to skip duplicates.
# That's much easier with a sorted array. So let's start by sorting.

# Double check syntax on this
# nums_sorted = sorted(nums)

# solution: List[List[int]] = []

# Looping:
# i starts at 0
# Break when nums_sorted[i] > 0 because they can't add up to 0 anymore

# Need better way to declare this
# Might not even need these dumb variables, not sure

# for i in range(len(nums_sorted)):
    # if nums_sorted[i] > 0:
        # break

    # Fix the third digit as nums_sorted[i]
    # if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
        # continue

    # left = i + 1
    # right = len(nums_sorted) - 1

    # while right > left:

        # num_right = nums_sorted[right]
        # num_left = nums_sorted[left]

        # needed_sum = 0 - nums_sorted[i]
        
        # left_plus_right = num_right + num_left

        # if left_plus_right == needed_sum:
            # solution.append([nums_sorted[i], num_left, num_right])
            # left +=1
            # right -=1

            # while left < right and nums_sorted[left] == nums_sorted[left - 1] and left > i + 1:
                # left += 1

            # while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                # right -= 1

        # else if left_plus_right > needed_sum:
            # rght -= 1

        # else:
            # left += 1



# return solution