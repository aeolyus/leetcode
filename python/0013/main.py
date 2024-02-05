class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for i, c in enumerate(s):
            if i < len(s) - 1 \
                    and conversion_map[s[i]] < conversion_map[s[i + 1]]:
                result -= conversion_map[s[i]]
            else:
                result += conversion_map[s[i]]
        return result
