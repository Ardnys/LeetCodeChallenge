from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node, count):
            if not node:
                return 0
            if node.val >= low and node.val <= high:
                count += node.val
            if node.left:
                count = traverse(node.left, count)
            if node.right:
                count = traverse(node.right, count)

            return count

        return traverse(root, 0)
