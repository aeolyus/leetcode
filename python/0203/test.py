import unittest
from main import Solution, ListNode


class Test0203(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]],
            [[], 1, []],
            [[7, 7, 7, 7], 7, []],
        ]

        for i in testcases:
            lst, val, expected = i
            prev = None
            head = None
            if lst:
                for i in lst[::-1]:
                    head = ListNode(i, prev)
                    prev = head
            s = Solution()
            new_head = s.removeElements(head, val)
            actual = []
            while new_head:
                actual.append(new_head.val)
                new_head = new_head.next
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
