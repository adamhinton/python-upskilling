# 94. Binary Tree Inorder Traversal
# Easy

# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []

        def recursive_helper(root: Optional[TreeNode]):
            if root is None:
                return
        
            recursive_helper(root.left)
            solution.add(root.val)
            recursive_helper(root.right)

        return solution
        