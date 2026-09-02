class Solution:
    # Time: O(n) - each character is pushed and popped at most once
    # Space: O(k) - stack and membership set hold at most k distinct letters (k <= 26)
    def remove_duplicate_letters(self, s: str) -> str:
        last_index = {char: i for i, char in enumerate(s)}
        stack: list[str] = []
        in_stack: set[str] = set()

        for i, char in enumerate(s):
            if char in in_stack:
                continue
            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(char)
            in_stack.add(char)

        return "".join(stack)
