import unittest
from typing import Optional, List
from main import Solution, ListNode


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
            list1 = list_to_linked_list(list1_lst)
            list2 = list_to_linked_list(list2_lst)
            actual = linked_list_to_list(s.mergeTwoLists(list1, list2))
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
