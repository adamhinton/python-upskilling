# 56. Merge Intervals
# Medium
# https://leetcode.com/problems/merge-intervals/description/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List, Tuple

class Solution:
    def merge(self, intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        solution = []

        return solution