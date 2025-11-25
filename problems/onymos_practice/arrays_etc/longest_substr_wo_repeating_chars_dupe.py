# Doing this again for practice

# 3. Longest Substring Without Repeating Characters
# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        return max_length

    
# PLAN:
# Time: O(n) one pass
# Space: O(n)
# Need:
    # Counter
    # Two pointer sliding window, start at 0 and 1

# if len(s) <= 1 return len(s)
# max_length = 0
# left, right = 0,1
# Initialize counter with count[s[left]]

# while right < len(s):
    # increment counter[right val]
    
    # while counter[right val] > 1:
        # decrement counter of left val
        # left++
        # This will ensure there are no dupes in substring

    # current_length = right - left + 1
    # max_lenght is max of max length and current length

# return max_length

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
print(solution.lengthOfLongestSubstring("bbbbb")) # 1
print(solution.lengthOfLongestSubstring("pwwkew")) # 3
