from typing import List
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        count = defaultdict(int)
        banned_set = set(banned)
        for s in symbols:
            paragraph = paragraph.replace(s, " ")
        for word in paragraph.lower().split():
            if word not in banned_set:
                count[word] += 1
        print(count.items())
        return max(count.items(), key=lambda i: i[1])[0]
