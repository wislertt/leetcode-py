class Solution:
    # Time: O(n)
    # Space: O(n)
    def smallest_number(self, pattern: str) -> str:
        result: list[str] = []
        stack: list[str] = []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    result.append(stack.pop())
        return "".join(result)
