import unittest
from main import Solution
from python.lib.list import ListNode


class Test0024(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4], [2, 1, 4, 3]],
            [[], []],
            [[1], [1]],
        ]

        for i in testcases:
            lst, expected = i
            head = ListNode.list_to_linked_list(lst)
            s = Solution()
            new_head = s.swapPairs(head)
            actual = ListNode.linked_list_to_list(new_head)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
