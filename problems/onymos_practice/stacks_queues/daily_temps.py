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
        solution = [0] * len(temperatures)
        mono_stack = []

        for idx, temp in temperatures[::-1]:
            while mono_stack and temperatures[mono_stack[-1]] <= temp:
                mono_stack.pop()

            solution[idx] = 0 if not mono_stack else (mono_stack[-1] - idx)

            mono_stack.append(idx)

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

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(solution.dailyTemperatures([30,60,90])) # [1,1,0]

