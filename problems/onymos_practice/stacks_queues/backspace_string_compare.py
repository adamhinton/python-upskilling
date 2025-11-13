# 844. Backspace String Compare

# Given two strings s and t, 
# return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(my_string: str) -> str:
            s_stack = deque([])

            for char in my_string:
                if char == "#" and s_stack:
                    s_stack.pop()
                elif char != "#":
                    s_stack.append(char)
                # Does nothing if char is # and s_stack is empty; this is intended
            
            return "".join(s_stack)

        s_backspaced = helper(s)
        t_backspaced = helper(t)

        return s_backspaced == t_backspaced
            
# PLAN
# Use stack

# t_stack, s_stack = deque([])

# Helper function that does this:
# for char in s_stack and t_stack:
    # if char == "#":
        # stack.pop()
    # else:
        # append char to stack
    # return stack.join()

# Perform helper function on both
# Compare stacks
