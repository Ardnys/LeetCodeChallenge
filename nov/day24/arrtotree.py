# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    right = len(nums)

    if not right:
        return None

    mid = int(right / 2)

    return TreeNode(
        nums[mid],
        sortedArrayToBST(nums[:mid]),
        sortedArrayToBST(nums[mid + 1 :]),
    )
