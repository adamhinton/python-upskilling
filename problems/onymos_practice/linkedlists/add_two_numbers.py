# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode(5)
        return solution
    
# PLAN
# Time complexity: O(n)
# Space complexity: O(n)
    # Could probably do this O(1) if needed
    # But the max LL length is 100 so seems unnecessary

# Two queues:
    # l1_queue, l2_queue
# Could do this appending to a simple list and reverse it later, but I find this simpler

# Do this for l1 and l2
# current_node = l1
# while current_node.val is not None:
    # val = current_node.val
    # l1_queue.appendleft(val)  >>> do the same with l2 and l2_queue

# Do this for l1_queue and l2_queue
    # Join in to a string, adding one digit at a time
    # Convert string to integer

# return l1 integer plus l2 integer