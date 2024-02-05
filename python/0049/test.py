import unittest
from main import Solution


class Test0049(unittest.TestCase):
    def test(self):
        testcases = [
            [
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ],
            [
                [""],
                [[""]],
            ],
            [
                ["a"],
                [["a"]],
            ],
        ]

        for i in testcases:
            strs, expected = i
            s = Solution()
            actual = s.groupAnagrams(strs)
            actual = sorted(sorted(lst) for lst in actual)
            expected = sorted(sorted(lst) for lst in expected)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
