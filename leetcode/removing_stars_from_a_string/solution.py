class Solution:
    # Time: O(n)
    # Space: O(n)
    def remove_stars(self, s: str) -> str:
        chars: list[str] = []
        for ch in s:
            if ch == "*":
                chars.pop()
            else:
                chars.append(ch)
        return "".join(chars)
