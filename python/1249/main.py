class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_lst = list(s)
        stack = []
        for i, ch in enumerate(s_lst):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s_lst[i] = ''
        while stack:
            s_lst[stack.pop()] = ''
        return ''.join(s_lst)
