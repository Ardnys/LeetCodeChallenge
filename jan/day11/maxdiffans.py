from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        # do it with one recursion

        def dfs(node):
            if not node:
                return
            diff(node, node.val)
            dfs(node.left)
            dfs(node.right)

        def diff(node, parent_val):
            if not node:
                return
            self.mx = max(self.mx, abs(parent_val - node.val))
            diff(node.left, parent_val)
            diff(node.right, parent_val)

        dfs(root)
        return self.mx
