class Solution:
    # Time: O(n)
    # Space: O(n)
    def parse_ternary(self, expression: str) -> str:
        stack: list[str] = []
        for ch in reversed(expression):
            if stack and stack[-1] == "?":
                stack.pop()
                true_val = stack.pop()
                stack.pop()  # ':'
                false_val = stack.pop()
                stack.append(true_val if ch == "T" else false_val)
            else:
                stack.append(ch)
        return stack[0]
