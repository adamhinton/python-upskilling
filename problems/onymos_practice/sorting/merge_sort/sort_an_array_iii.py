from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def recursive_helper(nums: List[int]):
            if len(nums) > 1: # Base 0base, move back up tree if not
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