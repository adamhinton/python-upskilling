# 2. Add Two Numbers
# Medium 

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional

class ListNode: 
    def __init__(self, val: int = 0, next = None):
        self.val = val  
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def recursive_helper(l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0):

            if l1 is None and l2 is None and carry == 0:
                return None
            
            solution = carry

            if l1 is not None:
                solution += l1.val
                l1 = l1.next

            if l2 is not None:
                solution += l2.val
                l2= l2.next
            
            result = ListNode(solution % 10)
            remainder = solution // 10

            result.next = recursive_helper(l1, l2, remainder)

            return result


        return recursive_helper(l1, l2, 0)
        

# PLAN:
# Time: O(n) - which we already did
    # But: One pass
    # reverse is a gift
    # add digit by digit smallest to largest    
# Space - O(n)
    # Just like before

# Need:     
    # Recursion 
    # Basic math - third grade arithmetic

# Basic idea:
    # You can add numbers back to front!    
    # 631 + 219: 1 + 9, then 3 + 1, 6 + 2
        # Carry over remainder - that's what the recursion is for!
        # recursive helper takes in a remainder
# In rcursive helper:
    # base case:
        # l1 and l2 don't exist

    # taking in digits one by one

     # Add sum % 10 to result
    # set l1 and l2 to to next
    # recursive_helper(l1, l2, sum// 10)

# return result

# Improvements:
    # One pass
    # Realizing that we don't have to build the number backwards
    # Don't need to convert in to string and reverse 

    # Insights:
        # One pass
        # reverse is a gift - helps us add the items together
        # Realizing we don't have to build the number backwards

# Regex:
    # Can we build `valid parentheses` with regex?
    # No:
    # regex can't handle arbitrary depth
    # can't pop or add to stack
    # fixed structure - adding and deletion
    # it matches patterns, rather than enforcing structre