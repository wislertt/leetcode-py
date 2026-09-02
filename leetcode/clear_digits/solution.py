class Solution:
    # Time: O(n)
    # Space: O(n)
    def clear_digits(self, s: str) -> str:
        stack: list[str] = []
        for char in s:
            if char.isdigit():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
