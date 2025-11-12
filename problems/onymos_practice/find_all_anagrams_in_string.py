# 438. Find all anagrams in a string
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# Given two strings s and p, 
# return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        solution = []
        if len(s) < len(p): return solution

        counter_p = Counter(p)
        counter_s = Counter(s[:len(p)])

        left = 0
        right = len(p) -1

        while right < len(s):
            if counter_p == counter_s:
                solution.append(left)
            
            counter_s[s[left]] -=1
            if counter_s[s[left]] == 0:
                del counter_s[s[left]]
            left+=1
            right +=1
            # Hacky solution to make sure we don't get index error at end of string
            # could optimize this better
            if right < len(s):
                counter_s[s[right]] = counter_s.setdefault(s[right], 0) + 1

        return solution
    

# PLAN:
# Not sure time complexity
# Definitely not O(n^2)
# Want to do O(n); maybe it'll be O(n * k) or something like that

# NEED:
# Counter probably - frequencies of letters. Definitely of p, maybe s too?
# Fixed sliding window - of length len(p)

# counter_p = Counter(p)
# counter_s = Counter(first len(p) chars of s)

# solution = []

# if len(s) < len(p) reutrn solution

# left = 0
# right = len(p) - 1

# while right < len(s):
    # if counter_p == counter_s: 
        # return left index (aka starting index of anagram)
        # O(len(p)) comparison; not sure if I can make an O(1) comparison happen
    # counter_s[s[left]] -= 1
    # left++
    # right++
    # counter_s[right] ++ if it exists; =1 if not

solution = Solution()
# print(solution.findAnagrams("cbaebabacd", "abc")) # [0,6]
print(solution.findAnagrams("abab", "ab")) # [0,1,2]