import unittest
from typing import List, Optional
from main import Solution, ListNode


class Test0023(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]],
            [[], []],
            [[[]], []],
        ]

        for i in testcases:
            arr_lists, expected = i
            lists = map(list_to_linked_list, arr_lists)
            s = Solution()
            actual = linked_list_to_list(s.mergeKLists(lists))
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
