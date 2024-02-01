from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log: str):
            identifier, content = log.split(" ", 1)
            if log[-1].isdigit():
                return (1,)
            else:
                identifier, content = log.split(" ", 1)
                return (0, content, identifier)
        return sorted(logs, key=custom_sort)
