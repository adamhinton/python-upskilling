# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

from typing import Dict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrome_length = 0

        tracker: Dict[str, int] = {}
        odd_numbers_count = 0

        for char in s:
            if tracker.get(char) is None:
                tracker[char] = 1
                odd_numbers_count += 1
            else:
                odd_numbers_count -= 1
                tracker[char] = 0
                palindrome_length += 2

        return palindrome_length
    
solution = Solution() 
print(solution.longestPalindrome("abccccdd")) # 7
print(solution.longestPalindrome("a")) # 1



# PLAN
# O(n)
# Need:
# palindrome_length = 0
# Hash table `tracker` - count of letters that haven't been added to palindrome_length
# odd_numbers_count = 0   >>> if there's 1 of any letter when all letters have been paired off, palindrome_length can increase by 1 
    # i.e. "abbadabba", you only need one "d" because it's in the middle

# for char in s:
    # if tracker.get(char) is None:
        # tracker[char] = 1
        # odd_numbers_count += 1
    # else: >>> char is already in tracker
        # odd_numbers_count -= 1
        # tracker[char] = 0
        # palindrome_length += 2