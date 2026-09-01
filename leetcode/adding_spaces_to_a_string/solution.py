class Solution:
    # Time: O(n + m) where n = len(s), m = len(spaces)
    # Space: O(n + m) for the output
    def add_spaces(self, s: str, spaces: list[int]) -> str:
        parts: list[str] = []
        prev = 0
        for idx in spaces:
            parts.append(s[prev:idx])
            prev = idx
        parts.append(s[prev:])
        return " ".join(parts)
