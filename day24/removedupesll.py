# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(head):
    if head is None:
        return head
    if head.next is None:
        return head
    prev = head
    current = head.next

    while current is not None:
        if prev.val == current.val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return head
