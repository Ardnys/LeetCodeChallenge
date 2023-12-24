from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.insert(0, root)
        view = []
        while queue:
            node = queue.pop()
            left_yes, right_yes = False, False

            if node.left:
                left_yes = True
                queue.insert(0, node.left)

            if node.right:
                right_yes = True
                queue.insert(0, node.right)
            if right_yes:
                view.append(node.right)
            elif left_yes:
                view.append(node.left)

        return view
