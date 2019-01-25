class Solution:
    def sim(s1, s2):
        same = ""
        length = min(len(s1), len(s2))
        for i in range(length):
            if s1[i] == s2[i]:
                same += s1[i]
            else:
                break
        return same

    def longestCommonPrefix(self, strs):
        pre = ""
        if strs:
            pre = strs[0]
            for word in strs:
                pre = Solution.sim(pre, word)
        return pre
