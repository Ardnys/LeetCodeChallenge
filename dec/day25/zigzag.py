from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

        def dfs(root, depth, is_left):
            if not root:
                self.depth = max(self.depth, depth)
                return

            dfs(root.left, depth + 1 if is_left == 'R' else 0, 'L')
            dfs(root.right, depth + 1 if is_left == 'L' else 0, 'R')

        dfs(root, 0, None)
        return self.depth
