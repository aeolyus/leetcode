from typing import Optional
from python.lib.list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        curr = head
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        return curr
