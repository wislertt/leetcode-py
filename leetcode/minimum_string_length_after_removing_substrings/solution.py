class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_length(self, s: str) -> int:
        stack: list[str] = []
        for char in s:
            if stack and ((stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D")):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
