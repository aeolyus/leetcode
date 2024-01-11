from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        head = None
        h = head
        carry = 0
        while l1 or l2:
            sm = carry
            if l1:
                sm += l1.val
            if l2:
                sm += l2.val
            carry = sm//10
            val = sm % 10
            node = ListNode(val)
            if head is None:
                head = node
            else:
                h.next = node
            h = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            h.next = ListNode(carry)
        return head
