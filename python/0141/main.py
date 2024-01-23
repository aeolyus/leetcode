from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
