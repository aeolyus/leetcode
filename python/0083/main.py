from typing import Optional
from python.lib.list import ListNode


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
