from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next

        head = None
        prev = None

        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            if head is None:
                head = node
            elif prev:
                prev.next = node
            prev = node
        return head
