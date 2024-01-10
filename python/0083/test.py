import unittest
from main import Solution, ListNode


class Test0083(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 1, 2], [1, 2]],
            [[1, 1, 2, 3, 3], [1, 2, 3]],
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
            new_head = s.deleteDuplicates(head)
            actual = None
            while new_head:
                if not actual:
                    actual = []
                actual.append(new_head.val)
                new_head = new_head.next
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
