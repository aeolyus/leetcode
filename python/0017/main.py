from typing import List

digit_map = {
    "2": [c for c in "abc"],
    "3": [c for c in "def"],
    "4": [c for c in "ghi"],
    "5": [c for c in "jkl"],
    "6": [c for c in "mno"],
    "7": [c for c in "pqrs"],
    "8": [c for c in "tuv"],
    "9": [c for c in "wxyz"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for c in digits:
            result = self.combo(result, digit_map[c])
        return result

    def combo(self, a: List[str], b: List[str]) -> List[str]:
        result = []
        if len(a) <= 0:
            return b
        for i in a:
            for j in b:
                result.append(i + j)
        return result
