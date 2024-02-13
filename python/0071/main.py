class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr_dir = ""
        for c in path + "/":
            if c != "/":
                curr_dir += c
            else:
                if curr_dir in ["", "."]:
                    pass
                elif curr_dir == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(curr_dir)
                curr_dir = ""
        result = "/" + "/".join(stack)
        return result
