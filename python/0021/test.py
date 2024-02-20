import unittest
from main import Solution
from python.lib.list import ListNode


class Test0021(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
            [[], [], []],
            [[], [0], [0]],
        ]

        for i in testcases:
            list1_lst, list2_lst, expected = i
            s = Solution()
            list1 = ListNode.list_to_linked_list(list1_lst)
            list2 = ListNode.list_to_linked_list(list2_lst)
            actual = ListNode.linked_list_to_list(
                s.mergeTwoLists(list1, list2)
            )
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
