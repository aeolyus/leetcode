import unittest
from main import Solution


class Test0929(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [
                    "test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com"
                ],
                2,
            ],
            [
                [
                    "a@leetcode.com",
                    "b@leetcode.com",
                    "c@leetcode.com",
                ],
                3,
            ],
        ]

        for i in testcases:
            emails, expected = i
            s = Solution()
            actual = s.numUniqueEmails(emails)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
