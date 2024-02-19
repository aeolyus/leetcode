from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_linked_list(lst: List) -> Optional['ListNode']:
        prev = None
        head = None
        if lst:
            for i in lst[::-1]:
                head = ListNode(i, prev)
                prev = head
        return head

    @staticmethod
    def linked_list_to_list(head: Optional['ListNode']) -> List:
        actual = []
        while head:
            actual.append(head.val)
            head = head.next
        return actual
