from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def uh(node, val):
            if node is None:
                return val
            val = uh(node.next, val)
            if val == 0:
                if node.next:
                    node.next = node.next.next
                else:
                    node.next = None
            return val - 1

        if uh(head, n) == 0:
            if head.next:
                head = head.next
            else:
                head = None
        return head
