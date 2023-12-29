from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left

        return root

    # one liner recursive
    def searchRecursiveBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        return (
            root
            if not root or root.val == val
            else self.searchRecursiveBST(
                root.right if root.val < val else root.left, val
            )
        )
