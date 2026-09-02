class Solution:
    # Time: O(n)
    # Space: O(n)
    def make_good(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
