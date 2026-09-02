class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverse_str(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i : i + k] = reversed(chars[i : i + k])
        return "".join(chars)
