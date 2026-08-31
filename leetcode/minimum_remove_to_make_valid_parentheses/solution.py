class Solution:
    # Time: O(len(s))
    # Space: O(len(s))
    def min_remove_to_make_valid(self, s: str) -> str:
        chars = list(s)
        stack: list[int] = []
        for i, char in enumerate(chars):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""
        for i in stack:
            chars[i] = ""
        return "".join(chars)
