from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_lenght = 0
        curr = head
        while curr:
            # print(f"val: {curr.val} at: {list_lenght}")
            list_lenght += 1
            curr = curr.next

        mid = list_lenght // 2

        curr = head
        prev = None
        for i in range(list_lenght):
            if i >= mid:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            else:
                curr = curr.next
        curr = head
        max_val = 0
        for i in range(mid):
            sum = curr.val + prev.val
            # print(f"sum: {sum} max: {max_val}")
            if sum >= max_val:
                max_val = sum
            curr = curr.next
            prev = prev.next

        return max_val


sol = Solution()
ll = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
sol.pairSum(ll)
