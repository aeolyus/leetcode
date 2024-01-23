import unittest
from typing import Optional, List
from main import Solution, ListNode


class Test0206(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
            [[1, 2], [2, 1]],
            [[], []],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            head = list_to_linked_list(lst)
            actual = linked_list_to_list(s.reverseList(head))
            self.assertEqual(expected, actual)


def list_to_linked_list(lst: List) -> Optional[ListNode]:
    prev = None
    head = None
    if lst:
        for i in lst[::-1]:
            head = ListNode(i, prev)
            prev = head
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List:
    actual = []
    while head:
        actual.append(head.val)
        head = head.next
    return actual


if __name__ == '__main__':
    unittest.main()
