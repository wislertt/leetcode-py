class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_valid(self, code: str) -> bool:
        if not code.startswith("<"):
            return False
        stack: list[str] = []
        i = 0
        n = len(code)
        while i < n:
            if stack and code.startswith("<![CDATA[", i):
                end = code.find("]]>", i)
                if end == -1:
                    return False
                i = end + 3
            elif code.startswith("</", i):
                end = code.find(">", i)
                if end == -1:
                    return False
                name = code[i + 2 : end]
                if not stack or stack[-1] != name:
                    return False
                stack.pop()
                i = end + 1
                if not stack and i != n:
                    return False
            elif code.startswith("<", i):
                end = code.find(">", i)
                if end == -1:
                    return False
                name = code[i + 1 : end]
                if not (1 <= len(name) <= 9 and name.isalpha() and name.isupper()):
                    return False
                stack.append(name)
                i = end + 1
            else:
                i += 1
        return not stack
