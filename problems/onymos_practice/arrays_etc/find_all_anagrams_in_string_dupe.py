# Doing this again for practice

# 438. Find All Anagrams in a String
# Medium
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        solution = []
        len_s = len(s)
        len_p = len(p)

        if len_p > len_s:
            return []

        counter_s = Counter(s[:len_p])
        counter_p = Counter(p)

        left, right = 0, len_p - 1

        while (left < len_s - len_p + 1):
            # We do updates to counter_s at the end of the previous iteration
            if counter_s == counter_p:
                solution.append(left)

            val_left = s[left]

            counter_s[val_left] -= 1
            
            left += 1
            right +=1

            if right < len_s:
                val_right = s[right]
                counter_s[val_right] += 1


        return solution
    
# PLAN
# Time: O(n)
# Space: O(1) I think, just need to build Counters

# len_s, len_p

# counter_s, counter_p
    # build counter_s from first len_p items in s

# left = 0
# right - len_p - 1

# while right < len(s) - len_p (-1? not sure):
    # subtract 1 from len_s[left-1] in counter_s
    # add 1 to len_s[right +1] in counter_s

    # if counter_s == counter_p, solution.append(left
    
    # Possible optimization:
        # This compares the entire counters every time
        # Can that be improved?
        # I'll get a solution working first.

    # left++, right++

solution = Solution()
# print(solution.findAnagrams("cbaebabacd", "abc"))
# # [0,6]

# print(solution.findAnagrams("abab", "ab"))
# # [0,1,2]

print(solution.findAnagrams("aa", "bb"))
# []

