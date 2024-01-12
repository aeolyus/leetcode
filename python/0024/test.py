import unittest
from typing import Optional, List
from main import Solution, ListNode


class Test0024(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4], [2, 1, 4, 3]],
            [[], []],
            [[1], [1]],
        ]

        for i in testcases:
            lst, expected = i
            head = self.list_to_linked_list(lst)
            s = Solution()
            new_head = s.swapPairs(head)
            actual = self.linked_list_to_list(new_head)
            self.assertEqual(expected, actual)

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
