# You are given two non-empty linked lists 
#   representing two non-negative integers. 
# The digits are stored in reverse order, 
#   and each of their nodes contains a single digit.
#   Add the two numbers and return the sum as a linked list in REVERSE ORDER. 
#
# You may assume the two numbers do not contain any leading zero, 
#   except the number 0 itself.
 
# Example 1:

# PLAN:
# O(n) memory
# O(n) space

# solution

# we need:
    # linkedlist
    # builder

    # for both LLs:
        # build a queue of integers in some way
     # join queue backwards in to string
            # make int from string
# Add sums together

# convert sum back in to a string
    # loop over BACKWARDS:
        # next node is added to the LL as the next val

# return solution

 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
 
# Constraints:
# 	• 0 <= Node.val <= 9
# Length of LL:
    #

#Edge cases:
    # empty:no
    # Negative: no

class Solution:
    def solve(self, input):
        # plan goes here
        return
    
# Linked lists