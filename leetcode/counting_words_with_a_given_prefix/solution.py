class Solution:
    # Time: O(sum(len(w) for w in words) * len(pref)) worst case via startswith
    # Space: O(1)
    def prefix_count(self, words: list[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))
