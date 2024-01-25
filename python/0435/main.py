from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        result = 1
        for interval in intervals:
            if prev[1] <= interval[0]:
                prev = interval
                result += 1
        return len(intervals) - result
