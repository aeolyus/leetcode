from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        h = head
        while h.next:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next
        return head
