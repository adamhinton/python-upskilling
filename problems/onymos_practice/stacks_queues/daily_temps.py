# 739. Daily Temperatures

# https://leetcode.com/problems/daily-temperatures/description/

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] 
#   is the number of days you have to wait after the ith day 
#   to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return [0]
    
# PLAN:
# O(n)

# Need:
# Monotonic stack to track indices in decreasing order

# solution = []
# mono_stack = []  >>> initialize with all zeros

# for idx, temp in temperatures[::-1]
    # while mono_stack and temperatures[mono_stack[-1]] <= temp:
        # mono_stack.pop()
    
    # If any temps left in stack, solution[idx] = mono_stack[-1] - idx
    # If no temps left in stack, solution[idx] = 0 >>> don't need to do this since it's actually 0, but I like the clarity

    # push idx in to mono_stack

