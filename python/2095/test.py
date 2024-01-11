import unittest
from main import Solution, ListNode


class Test2095(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]],
            [[1, 2, 3, 4], [1, 2, 4]],
            [[2, 1], [2]],
        ]

        for i in testcases:
            lst, expected = i
            prev = None
            head = None
            if lst:
                for i in lst[::-1]:
                    head = ListNode(i, prev)
                    prev = head
            s = Solution()
            new_head = s.deleteMiddle(head)
            actual = []
            while new_head:
                actual.append(new_head.val)
                new_head = new_head.next
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
