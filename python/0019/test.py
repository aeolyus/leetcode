import unittest
from main import Solution, ListNode


class Test0019(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
            [[1], 1, []],
            [[1, 2], 1, [1]],
            [[1, 2], 2, [2]],
        ]

        for i in testcases:
            lst, n, expected = i
            prev = None
            head = None
            if lst:
                for i in lst[::-1]:
                    head = ListNode(i, prev)
                    prev = head
            s = Solution()
            new_head = s.removeNthFromEnd(head, n)
            actual = []
            while new_head:
                actual.append(new_head.val)
                new_head = new_head.next
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
