from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.pafs = []

        def dfs(root, target, nodes):
            if not root:
                return
            nodes.append(root.val)
            if not root.left and not root.right and target == root.val:
                self.pafs.append([node for node in nodes])

            dfs(root.left, target - root.val, nodes)
            dfs(root.right, target - root.val, nodes)
            nodes.pop()

        dfs(root, targetSum, [])
        return self.pafs
