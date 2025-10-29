# https://leetcode.com/problems/remove-linked-list-elements/description/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
# and return the new head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val_to_remove: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        current_node = dummy_node

        while current_node.next: 
            if current_node.next.val == val_to_remove:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_node.next
    

# PLAN
# Should be O(n) memory and I think O(1) space

# Make a dummy node; that node's next is head
# Make a current node equal to dummy

# while current.next.val == val_to_remove:
# current.next = current.next.next
# else:
# current.next = current.next.next

# return dummy.next

