from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        uh = set()
        node = headA
        while node:
            uh.add(node)
            node = node.next

        node = headB
        while node:
            if node in uh:
                return node
            node = node.next

        return None
