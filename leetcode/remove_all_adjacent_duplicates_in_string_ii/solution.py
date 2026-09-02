class Solution:
    # Time: O(len(s))
    # Space: O(len(s))
    def remove_duplicates(self, s: str, k: int) -> str:
        stack: list[tuple[str, int]] = []
        for char in s:
            if stack and stack[-1][0] == char:
                char, count = stack[-1]
                if count + 1 == k:
                    stack.pop()
                else:
                    stack[-1] = (char, count + 1)
            else:
                stack.append((char, 1))
        return "".join(char * count for char, count in stack)
