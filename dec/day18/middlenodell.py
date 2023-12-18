from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        ctr = 0
        current = head

        while current:
            current = current.next
            ctr += 1

        mid = ctr // 2
        print(f"ctr = {ctr} mid: {mid}")
        current = head
        for i in range(mid - 1):
            current = current.next
        if current.next:
            current.next = current.next.next

        return head
