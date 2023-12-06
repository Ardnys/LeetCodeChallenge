from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ctr = 0
        current = head

        while current and ctr < k:
            current = current.next
            ctr += 1

        if ctr < k:
            return head

        prev, current = None, head
        for _ in range(k):
            next = current.next
            current.next = prev
            prev = current
            current = next

        head.next = self.reverseKGroup(current, k)
        return prev


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.reverseKGroup(head, 2)
