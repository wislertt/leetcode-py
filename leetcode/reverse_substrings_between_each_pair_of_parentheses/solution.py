class Solution:
    # Time: O(n^2) worst case, O(n) average
    # Space: O(n)
    def reverse_parentheses(self, s: str) -> str:
        stack: list[str] = []
        for char in s:
            if char == ")":
                segment: list[str] = []
                while stack and stack[-1] != "(":
                    segment.append(stack.pop())
                stack.pop()
                stack.extend(segment)
            else:
                stack.append(char)
        return "".join(stack)
