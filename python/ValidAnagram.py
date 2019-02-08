class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t):
            return False
        temp = [0 for i in range(26)]
        for l in s:
            temp[ord(l) - ord('a')] += 1
        for l in t:
            temp[ord(l) - ord('a')] -= 1
        return all(v == 0 for v in temp)
