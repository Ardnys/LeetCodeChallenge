from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pafs = 0

        def traverse(root, target):
            if not root:
                return
            findSum(root, target)
            traverse(root.left, target)
            traverse(root.right, target)

        def findSum(root, target):
            if not root:
                return
            if root.val == target:
                self.pafs += 1

            findSum(root.left, target - root.val)
            findSum(root.right, target - root.val)

        traverse(root, targetSum)
        return self.pafs
