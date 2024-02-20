from typing import Optional
from python.lib.list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        b = head
        while a and b:
            a = a.next
            b = b.next
            if b and b.next:
                b = b.next
            else:
                return False
            if a == b:
                return True
        return False
