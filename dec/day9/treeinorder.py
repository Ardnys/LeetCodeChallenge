from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])

    def helper(self, root, traversal_list):
        if root is None:
            return traversal_list
        self.helper(root.left, traversal_list)
        traversal_list.append(root.val)
        self.helper(root.right, traversal_list)
        return traversal_list
