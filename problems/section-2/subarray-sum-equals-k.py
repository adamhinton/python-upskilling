# Given an array of integers nums and an integer k, 
#   return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List, Dict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarrays_solution = 0
        prefix_sums_seen: Dict[int, int] = {0:1}
        
        current_sum = 0

        for num in nums:
            current_sum += num
            needed_sum =current_sum - k

            total_subarrays_solution += prefix_sums_seen.get(needed_sum, 0)

            prefix_sums_seen[current_sum] = prefix_sums_seen.get(current_sum, 0) + 1


        return total_subarrays_solution
    

# print(Solution().subarraySum(nums = [1,1,1], k = 2)) # 2
# print(Solution().subarraySum(nums = [1,2,3], k = 3)) # 2
print(Solution().subarraySum(nums = [1], k = 0)) # 2

# THOUGHTS before planning:
# -Should be O(n)
# Need prefix sum
# It'll be something like subtracting items in prefix_sum from k to see what we need

# PLAN:

# total_subarrays_solution = 0
# current_sum = 0
# prefix_sums_seen: Dict[int, int] = {}

# Update: I originally made prefix_sum separately, but I can do this problem in one pass

# for num in nums:
    # current_sum += num
    # needed_sum = current_sum - k

    # This comes first bc needed_sum could equal current_sum
        # So this could just be a valid subarray of length 1
    # prefix_sums_seen[current_sum] +=1 or = 1 (I forget syntax here)

    # if needed_sum in prefix_sums_seen:
        # total_subarrays_solution += prefix_sums_seen[needed_sum]

# return total_subarrays_solution


# for num in nums:
    # running_total += num
    # prefix_sum.append(running_total)
