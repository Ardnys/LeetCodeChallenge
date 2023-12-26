from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leafs = []
        self.index = 0
        self.flag = True

        def spring(node):
            if not node:
                return
            if not node.left and not node.right:
                self.leafs.append(node.val)

            spring(node.left)
            spring(node.right)

        def autumn(node):
            if not node:
                return
            if not node.left and not node.right:
                if self.index >= len(self.leafs):
                    self.flag = False
                    return
                if self.leafs[self.index] == node.val:
                    self.index += 1
                    return

                self.flag = False

            autumn(node.left)
            autumn(node.right)

        spring(root1)
        autumn(root2)
        return self.flag and self.index == len(self.leafs)
