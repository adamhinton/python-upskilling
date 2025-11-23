# Doing this again for review

# 739. Daily Temperatures
# Medium
# https://leetcode.com/problems/daily-temperatures/description/

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] 
#   is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [None for _ in range(len(temperatures))]

        return solution
    
# PLAN
# Time: O(n) one pass
# Space: O(n) - could maybe make it O(1) by modifying temps in place; seems unnecessary
# Need:
    # Monotonic stack - track next highest temperature
    # Loop backwards over temps

# solution = [] >> QUEUE of length len(temps)
# temp_stack = [] >>> holds INDEXES, not temperatures

# for idx, temp in (looping over temps backwards):
    # while temp_stack has vals and temp > the top temp of the stack
        # temp_stack.pop()

    # if there are values in stack:
        # days_waited = temp_stack[-1] - index
        # solution.appendleft[days_waited] >>> building backwards

    # else: >> no temps greater so far
        # solution.appendleft(0)

# return solution
    

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(solution.dailyTemperatures([30,60,90])) # [1,1,0]