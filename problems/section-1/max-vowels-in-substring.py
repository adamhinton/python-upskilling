# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# Given a string s and an integer k, 
#   return the maximum number of vowel letters 
#   in any substring of s with length k.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return 0



# Thoughts:
# - Sliding window (obviously)
# -Should be O(n)
# not sure why this is LC medium; seems easy enough. Maybe I'll find hidden complications.

print(Solution.maxVowels(s="abciiidef"), k=3)  # 3
print(Solution.maxVowels(s="aeiou"), k=2)  # 2
print(Solution.maxVowels(s="leetcode"), k=3)  # 2