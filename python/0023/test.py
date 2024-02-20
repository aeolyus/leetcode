import unittest
from typing import List, Optional
from main import Solution
from python.lib.list import ListNode


class Test0023(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]],
            [[], []],
            [[[]], []],
        ]

        for i in testcases:
            arr_lists, expected = i
            lists = map(ListNode.list_to_linked_list, arr_lists)
            s = Solution()
            actual = ListNode.linked_list_to_list(s.mergeKLists(lists))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
