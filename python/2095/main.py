from typing import Optional
from python.lib.list import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.len(head)
        if length <= 1:
            return None

        mid = length//2

        h = head
        i = 0
        while i < mid - 1:
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
