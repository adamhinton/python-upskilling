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

class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

from collections import deque

class Solution:
    def solve(self, node1: ListNode, node2: ListNode):
        arr1, arr2 = deque([]), deque([])
        
        node_1 = node1
        node_2 = node2
        while(node_1.val is not None):
            arr1.appendleft(str(node_1.val))
        
        while(node_2.val):
            arr2.appendleft(str(node_2.val))

        int_1 = int("".join(arr1))
        int_2 = int("".join(arr2))

        sum = int_1 + int_2

        # loop over sum, appendlefting each int to a linkedlist
        sum_string = str(sum)
        node = ListNode(sum[-1])
        solution = node # saving a reference to node
        for i in range(len(sum_string)-1, 0, -1):
            new_node = ListNode(int(sum_string[i]))
            node.next = new_node
            node = new_node


        return solution


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

node_1 = ListNode(2)
node_2 = ListNode(4)
node_3 = ListNode(3)
node_2.next = node_3
node_1.next = node_2

node_4 = ListNode(5)
node_5 = ListNode(6)
node_6 = ListNode(4)
node_4.next = node_5
node_5.next = node_6

solution = Solution()
print(solution.solve(node_1, node_2))

    
# Linked lists


    