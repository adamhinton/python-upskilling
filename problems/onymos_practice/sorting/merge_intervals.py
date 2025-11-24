# 56. Merge Intervals
# Medium
# https://leetcode.com/problems/merge-intervals/description/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List, Tuple

class Solution:
    def merge(self, intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(intervals) == 1: return intervals
        solution = []

        intervals.sort(lambda x: x[0])

        return solution
    
# PLAN
# Time: O(n log n)
# Space: O(n)
# Need:
    # Sorting
    # That's it, I think

# solution = []
# if solution is length 1, return intervals

# intervals.sort(by intvl[0])

# add intervals[0] to solution

# for start, end in intervals[1:]:  
    # last_end = intervals[-1][1]
    # if start <= last_end:
        # intervals[-1][1] = max(end, last_end)
        # 
    # else:
        # solution.append(start, end)

# return solution

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]])) # [[1,5]]
print(solution.merge([[4,7],[1,4]])) # [[1,7]]