# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        d = {}

        def traverse(root):
            if root == None:
                return
            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        uh = 0
        m = 0
        for key in d.keys():
            if d[key] > m:
                m = d[key]
                uh = key

        modes = [uh]
        for key in d.keys():
            if d[key] == m and key != uh:
                modes.append(key)
        return modes
