import unittest
from main import Solution, ListNode


class Test0141(unittest.TestCase):
    s = Solution()

    def test_example_1(self):
        head = ListNode(3)
        curr = head
        for i in [2, 0, 4]:
            curr.next = ListNode(i)
            curr = curr.next
        curr.next = head.next
        expected = True
        actual = self.s.hasCycle(head)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        head = ListNode(1)
        tail = ListNode(2)
        head.next = tail
        tail.next = head
        expected = True
        actual = self.s.hasCycle(head)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        head = ListNode(1)
        expected = False
        actual = self.s.hasCycle(head)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
