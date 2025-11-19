# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#   determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true
 
# Example 2:
# Input: s = "()[]{}"
# Output: true
 
# Example 3:
# Input: s = "(]"
# Output: false
 
# Constraints:
# s consists of parentheses only '()[]{}'.

class Solution:
    def solve(self, s):
        tracker = []
        parens = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        
    
# PLAN:
# Stack, hash table
# O(n) Time
# O(n) space --- stack

# stack = []
    # {
        # "}": "{",
        # ")": "(",
        # "]": "["
    # }
# for char in string:
    # if it's an opener (not in dict):
        # add it to the stack
    # if it's a closer:
        # pop from the stack
        # if popped value not corresponds to char: 
            # return False

# return True