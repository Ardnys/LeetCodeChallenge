
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.hallo(root, targetSum, 0, False)
        
    def hallo(self, node, targetSum, sum, yes):
        sm = sum + node.val
        if not node.left and not node.right:
            if sm == targetSum:
                yes = True
                return yes
            else:
                return yes
        if yes:
            return yes
        else:
            if node.left:
                l = self.hallo(node.left, targetSum, sm, yes)
                if l:
                    return l
            if node.right:
                r = self.hallo(node.right, targetSum, sm, yes)
                if r:
                    return r
        return yes
        
        


