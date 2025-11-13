# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.ß

from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        left = 0
        right = 1
        longest_sub = 1
        letter_set = set()

        l_str = s[left]
        r_str = s[right]

        letter_set.add(l_str)

        while right < len(s):
            l_str = s[left]
            r_str = s[right]

            while r_str in letter_set:
                letter_set.remove(s[left])
                left += 1
            
            letter_set.add(r_str)


            longest_sub = max(longest_sub, (right - left + 1))
            right +=1

        return longest_sub
    
solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
print(solution.lengthOfLongestSubstring("bbbbb")) # 1
print(solution.lengthOfLongestSubstring("pwwkew")) # 3

    

# Plan:
# O(n), one pass
# Need: 
    # Hash table (char and its last seen index)
    # Sliding window; start at 0 and 1

# if len(s) < 2 return len(s)

# tracker: Dict[str, int] = {} >>> last seen index of letter

# left = 0
# right = 1
# longest_sub = 1

# while left < right:
    # l_str = s[left]
    # r_str = s[right]

    # if r_str in tracker is greater than left:
        # left = tracker[r_str] + 1
        # tracker[r_str] = right
    
    # else:
        # longest_sub = max(longest_sub, right - left + 1)
        # right = min(right++, len(s) - 1)

# return longest_sub