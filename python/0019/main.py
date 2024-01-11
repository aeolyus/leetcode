from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self,
            head: Optional[ListNode],
            n: int,
    ) -> Optional[ListNode]:
        length = self.len(head)
        if length <= 1:
            return None

        to_remove = length - n

        if to_remove == 0:
            head = head.next
            return head

        h = head
        i = 0
        while i < to_remove - 1:
            h = h.next
            i += 1
        h.next = h.next.next
        return head

    def len(self, head: Optional[ListNode]):
        i = 0
        h = head
        while h:
            h = h.next
            i += 1
        return i
