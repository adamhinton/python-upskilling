# https://www.codewars.com/kata/5bcd90808f9726d0f6000091/python

# Description is too long to copy here, but TLDR:
# Params: string s. Contains letters, nus, symbols
# Find longest substring consisting of unique characters and return the substring's LENGTH

from typing import Dict

def longest_substring (s: str) -> int:

    str_length = len(s)
    if str_length <= 1:
        return str_length

    dupe_check: Dict[str, int] = {}
    longest_substring_length = 1

    left_index = 0

    for right_index in range(str_length):
        right_char = s[right_index]

        # This only cares about dupes in the current subarray
        if right_char in dupe_check and dupe_check[right_char] >= left_index:
            left_index = dupe_check[right_char] + 1

        dupe_check[right_char] = right_index
        longest_substring_length = max(longest_substring_length, right_index - left_index + 1)

    return longest_substring_length

print(longest_substring("baacab")) # 3
print(longest_substring("abcd")) # 4
print(longest_substring("hchzvfrkmlnozjk")) # 11

# PLAN:
# if len(s) is 1 or 0 return len(s)
# Sliding window, unfixed
# Dupe_check has a char key and the char's last-seen index as a value
# dupe_check: Dict[str, bool] = {}
# current_longest_substring_length = 1

# Now for looping. We know length is at least 2
# left = 0
# right = 1

# while right < len(s):
    # left_char is s[left]
    # right_char is s[right]

    # if right_char is in dupe_check:
        # move left pointer up to exclude the duplicate
        # left = dupe_check[right_char] + 1

    # else:
        # right += 1
        # if right - left is more than current_longest_substring_length, current_long... = right - left

# return current_longest_substring_length