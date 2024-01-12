class Solution:
    def partitionString(self, s: str) -> int:
        i = 1
        st = set()
        for c in s:
            if c in st:
                i += 1
                st = set()
            st.add(c)
        return i
