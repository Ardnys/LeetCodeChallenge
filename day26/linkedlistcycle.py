from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        uh = set()
        while node:
            if node in uh:
                return True
            uh.add(node)
            node = node.next
        return False


node = ListNode(2)
node.next = ListNode(3)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
# node.next.next.next.next = node.next

sol = Solution()
print(sol.hasCycle(node))
