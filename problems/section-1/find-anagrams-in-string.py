# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Note, couldn't find this in codewars

# Given two strings s and p, 
# return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.

from typing import List

class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return []
    

print(Solution().findAnagrams(s = "cbaebabacd", p = "abc")) # [0, 6]
print(Solution().findAnagrams(s = "abab", p = "ab")) # [0, 1, 2]

# PLAN
# Hmm, I wonder how to make this O(n). Right now I can compare each individual window to p which would be O(n * len(p))

# anagram_size = len(p)

# solution: List[int] = []

# Stop when our window will be too short 
# for i in range(n -anagram_size + 1):
    # curr_string = s[i, anagram_size]

    # if curr_string == p:
        # solution += i

# return i 
