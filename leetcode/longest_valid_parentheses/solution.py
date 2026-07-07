class Solution:
    # Time: O(n)
    # Space: O(n)
    def longest_valid_parentheses(self, s: str) -> int:
        max_length = 0
        # Stack of indices; seeded with -1 as the last "unmatched" position
        stack: list[int] = [-1]

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Unmatched ')', reset the base index
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
