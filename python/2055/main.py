from typing import List


class Solution:
    def platesBetweenCandles(
            self,
            s: str,
            queries: List[List[int]],
    ) -> List[int]:
        len_s = len(s)

        candle_count = 0
        num_candles = dict()

        # Map of closest left candle
        left_candle = [None] * len_s
        curr_left = None
        for i, c in enumerate(s):
            if c == "|":
                curr_left = i
                num_candles[i] = candle_count
                candle_count += 1
            left_candle[i] = curr_left

        # Map of closest right candle
        right_candle = [None] * len_s
        curr_right = None
        for i in range(len_s - 1, -1, -1):
            c = s[i]
            if c == "|":
                curr_right = i
            right_candle[i] = curr_right

        result = []
        for left, right in queries:
            l_candle = right_candle[left]
            r_candle = left_candle[right]
            if l_candle is not None \
                    and r_candle is not None \
                    and l_candle < r_candle:
                result.append(
                    r_candle
                    - l_candle
                    - num_candles[r_candle]
                    + num_candles[l_candle]
                )
            else:
                result.append(0)
        return result
