from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        tail = head
        nxt = head.next
        second = head.next
        current = nxt.next
        is_odd = True
        while current:
            if is_odd:
                tail.next = current
                tail = current
                is_odd = False
            else:
                nxt.next = current
                nxt = current
                is_odd = True
            current = current.next
        tail.next = second
        nxt.next = None

        return head
