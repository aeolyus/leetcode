import unittest
from main import Solution


class Test0874(unittest.TestCase):
    def test(self):
        testcases = [
            [[4, -1, 3], [], 25],
            [[4, -1, 4, -2, 4], [[2, 4]], 65],
            [[6, -1, -1, 6], [], 36],
        ]

        for i in testcases:
            commands, obstacles, expected = i
            s = Solution()
            actual = s.robotSim(commands, obstacles)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
