from typing import List, Optional
from sys import maxsize


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lenght = len(lists)
        indexes = [lists[i] for i in range(lenght)]
        current = hi = ListNode(0)

        while True:
            idx = 0
            uh = maxsize

            oops = False

            for i in range(len(indexes)):
                # print(f"checking {indexes[i].val}, what: {indexes[i] is not None}")
                if indexes[i] is not None and indexes[i].val < uh:
                    oops = True
                    uh = indexes[i].val
                    idx = i

            if not oops:
                # print("oops")
                break

            current.next = ListNode(indexes[idx].val)
            current = current.next
            # print(f"current boi: {boi}")

            # print(f"smol: {indexes[idx].val}")
            indexes[idx] = indexes[idx].next


        cur = sili = ListNode(0)
        return hi.next


sol = Solution()
l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
merged = sol.mergeKLists([l1, l2, l3])
while merged:
    print(merged.val)
    merged = merged.next
