from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        pass


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def make_num(node, tens=1):
            if not node:
                return 0
            if not node.next:
                return node.val * tens

            yes = make_num(node.next, tens * 10)
            yes += node.val * tens
            return yes

        def rev_num(num):
            if num <= 0:
                return None
            rem = num % 10
            yes = rev_num(num // 10)
            if not yes:
                return ListNode(rem)
            else:
                return ListNode(rem, yes)

        n1 = make_num(l1)
        n2 = make_num(l2)
        prod = n1 + n2

        rev_list = rev_num(prod)

        return rev_list


sol = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol.addTwoNumbers(l1, l2)
