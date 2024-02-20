from typing import List, Optional
import heapq
from python.lib.list import ListNode


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
