import unittest
from main import Solution
from python.lib.list import ListNode


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
                ListNode.list_to_linked_list(l1),
                ListNode.list_to_linked_list(l2),
            )
            self.assertEqual(expected, ListNode.linked_list_to_list(actual))


if __name__ == '__main__':
    unittest.main()
