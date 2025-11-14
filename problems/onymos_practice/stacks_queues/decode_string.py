# 394. Decode String
# https://leetcode.com/problems/decode-string/description/
# Level: Medium

# Given an encoded string, return its decoded string.

# The encoding rule is: 
# k[encoded_string], 
# where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; 
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits 
#   and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
        solution = []

        return "".join(solution)
    
# PLAN:
# O(n)
# one pass (then again to join the solution array together as string)

# solution = []

# idx = 0

# while idx < len(s) - 1:
    # char = s[idx]

    # if char isn't "[":
        # solution.append(char)
        # i++
        # continue

    # Char is "["
    # num_repetitions = solution[-1]
    #str_to_repeat = ""

    # get the full character to repeat
    # while s[idx] != "]"
        # current_char = s[idx]
        # str_to_repeat.append(current_char)
        # idx++
    
    # idx++ >>> get past the ]

    # now add str_to_repeat to solution num_repetitions times
