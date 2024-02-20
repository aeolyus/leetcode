import unittest
from main import Solution
from python.lib.list import ListNode


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
            head = ListNode.list_to_linked_list(lst)
            actual = ListNode.linked_list_to_list(s.reverseList(head))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
