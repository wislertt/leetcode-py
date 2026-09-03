class Solution:
    # Time: O(len(a) + len(b))
    # Space: O(len(a) + len(b))
    def repeated_string_match(self, a: str, b: str) -> int:
        min_repeats = -(-len(b) // len(a)) if b else 1
        for k in (min_repeats, min_repeats + 1):
            if b in a * k:
                return k
        return -1
