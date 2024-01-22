from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = None
        count = 0
        i = 0
        for c in chars + [" "]:
            if prev is None:
                prev = c
                count += 1
            elif prev == c:
                count += 1
            elif prev != c:
                chars[i] = prev
                if count > 1:
                    for n in [*str(count)]:
                        i += 1
                        chars[i] = n
                prev = c
                count = 1
                i += 1
        return i
