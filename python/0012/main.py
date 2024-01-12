NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        i = 0
        while num > 0:
            n = NUMS[i]
            if n <= num:
                num -= n
                result += ROMS[i]
            else:
                i += 1
        return result
