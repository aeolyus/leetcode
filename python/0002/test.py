import unittest
from typing import List, Optional
from main import Solution, ListNode


class Test0002(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
            [[0], [0], [0]],
            [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
        ]

        for i in testcases:
            l1, l2, expected = i
            s = Solution()
            actual = s.addTwoNumbers(
                self.list_to_linked_list(l1),
                self.list_to_linked_list(l2),
            )
            self.assertEqual(expected, self.linked_list_to_list(actual))

    def list_to_linked_list(self, lst: List) -> Optional[ListNode]:
        prev = None
        head = None
        if lst:
            for i in lst[::-1]:
                head = ListNode(i, prev)
                prev = head
        return head

    def linked_list_to_list(self, head: Optional[ListNode]) -> List:
        actual = []
        while head:
            actual.append(head.val)
            head = head.next
        return actual


if __name__ == '__main__':
    unittest.main()
